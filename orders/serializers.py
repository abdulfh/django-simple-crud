from rest_framework import serializers
from orders.models import Order
from cars.serializers import CarSerializers
from authentication.serializers import UserSerializers
class OrderSerializers(serializers.ModelSerializer):
    carId = CarSerializers(many=False)
    userId = UserSerializers(many=False)
    class Meta:
        model = Order
        fields = '__all__'

class OrderUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, value):
        if value['pickUpDate'] > value['dropOffDate']:
            raise serializers.ValidationError({"pickUpDate": "must lower than drop off date"})
        elif value['dropOffDate'] > value['pickUpDate']:
            raise serializers.ValidationError({"dropOffDate": "must higher than pick up date"})
        
        return value