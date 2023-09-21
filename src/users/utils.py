import jwt
from config import settings
from rest_framework.views import Response
from datetime import timedelta, datetime

class JwtHelper:
    @staticmethod
    def generate_jwt_token(user_id, secret_key, expires_in_minutes):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(minutes=expires_in_minutes)
        }
        return jwt.encode(payload, secret_key, algorithm='HS256')

