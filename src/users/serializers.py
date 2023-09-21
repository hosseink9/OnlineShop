from rest_framework import serializers

from .models import User
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
import random
from datetime import timedelta
from django.utils import timezone


class SerializerRegisterUser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','phone','username','first_name','last_name','address']

        def create(self, validated_data):
            password=validated_data.pop('password', None)
            instance=self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

class UserVerifySerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)