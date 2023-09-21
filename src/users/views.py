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



class SendOTPView(APIView):
    def post(self, request):
        serializer=SerializerLogin(data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.create_otp(request, serializer.data['phone'])
            return Response (data={'message':"200"})


class VerifyOTP(APIView):

    def post(self, request):
        serliazer=LoginOTPSerializer(data=request.data, context={'request':request})
        if serliazer.is_valid(raise_exception=True):
            user=User.objects.get(phone=request.session.get('phone'))
            access_token=user.get_access_token()
            refresh_token=user.get_refresh_token()
            return Response(data={'message':"success", "AT":access_token, "RT":refresh_token})


class LoginRequiredView(APIView):
    authentication_classes = [JwtAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request):
        return Response({'message':"success","phone":request.user.phone})
