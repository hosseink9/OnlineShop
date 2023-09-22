from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='user_register'),
    path('sendotp/',views.SendOTPView.as_view()),
    path('verify/', views.VerifyOTP.as_view()),
    path('requiredlogin/', views.LoginRequiredView.as_view()),
]