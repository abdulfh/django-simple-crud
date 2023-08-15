from django.urls import path
from admins import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register', views.register),
    path('login', TokenObtainPairView.as_view()),
]