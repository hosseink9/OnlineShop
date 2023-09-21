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


class SerializerLogin(serializers.Serializer):

    phone = serializers.CharField(required=True, allow_null=False)


    def validate(self, data):
        phone = data.get('phone')

        if not User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError



        return data

    @staticmethod
    def create_otp(request, phone):
        request.session["otp"] = random.randint(1000, 9999)
        request.session["otp_expire"] = (timezone.now() + timedelta(minutes=10)).strftime("%d/%m/%Y, %H:%M:%S")
        request.session['phone']=phone
        print(f"generated:{request.session['otp']}  until:{request.session['otp_expire']}")



