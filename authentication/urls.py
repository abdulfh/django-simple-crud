from django.urls import path
from authentication import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/register', views.admin_register),
    path('user/register', views.user_register),
    path('login', TokenObtainPairView.as_view()),
]