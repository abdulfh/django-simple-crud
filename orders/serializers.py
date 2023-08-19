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