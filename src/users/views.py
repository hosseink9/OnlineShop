from django.shortcuts import render
from .serializers import SerializerRegisterUser, SerializerLogin, LoginOTPSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .auth import JwtAuthentication
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):

    def post(self, request):
        serializer=SerializerRegisterUser(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):

    def post(self, request):
        phone = request.data['phone']
        password = request.data['password']

        user = User.objects.filter(phone=phone).first()

        if user is None:
            raise AuthenticationFailed('User is not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Password is not correct')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt':token
            }

        update_last_login(None, user)
        return response


class UserVerifyView(APIView):

    def get(self, request):
        if (not self.expiration_time) or (
            timezone.now() > timezone.datetime.strptime(self.expiration_time, "%d/%m/%Y, %H:%M:%S")
        ):
            request = generate_2fa(request)
        else:
            print(f"previous:{self.generated_otp}  until:{self.expiration_time}")
        return super().get(request)

    def post(self, request):
        if not all([self.generated_otp,self.expiration_time]):
            return Response("panel:user_verify")
        if timezone.now() > timezone.datetime.strptime(self.expiration_time, "%d/%m/%Y, %H:%M:%S"):
            print("expired")
            self.request = generate_2fa(request)
            form = self.get_form()
            form.add_error("otp", "Previous 2FA code expired. A new code has been sent to you")
            return self.form_invalid(form)
        else:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            return self.form_invalid(form)

    def form_valid(self, form):
        entered_otp = form.clean().get('otp')
        if entered_otp == str(self.generated_otp):
            self.request.session.pop('2FA')
            self.request.session.pop('2fa_expire')
            self.request.session["authenticated"] = True
            user = User.objects.get(phone=self.user_phone)
            login(self.request, user, "users.auth.UserAuthBackend")
            self.request.session['phone'] = user.phone
            return super().form_valid(form)
        else:
            form.add_error("otp","Invalid code entered")
            return self.form_invalid(form)