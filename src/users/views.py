from rest_framework.views import Response, APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import update_last_login
from rest_framework.views import Response
from django.contrib.auth import authenticate
from django.utils import timezone
from django.contrib.auth import login

import random
from datetime import timedelta
import jwt,datetime

from .models import User
from .serializers import UserSerializer,UserVerifySerializer


def generate_2fa(request):  # NOTE: This is not a view
    request.session["2FA"] = random.randint(1000, 9999)
    request.session["2fa_expire"] = (timezone.now() + timedelta(minutes=1)).strftime("%d/%m/%Y, %H:%M:%S")
    print(f"generated:{request.session['2FA']}  until:{request.session['2fa_expire']}")
    return request



class RegisterView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
