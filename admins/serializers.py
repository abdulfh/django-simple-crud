from rest_framework import serializers
from admins.models import Admin

class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
    
    def create(self, validated_data):
        admin = Admin.objects.create(email=validated_data['email'])
        admin.set_password(validated_data['password'])
        admin.save()
        return admin