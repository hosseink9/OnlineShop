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

# Create your views here.
