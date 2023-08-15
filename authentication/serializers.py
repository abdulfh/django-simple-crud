from rest_framework import serializers
from authentication.models import Admin,User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','username','zip','phoneNumber','city','message','address']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['email','password']
        
    def create(self, validated_data):
        validated_data['is_admin'] = True
        return Admin.objects.create_user(**validated_data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_admin'] = user.is_admin
        return token