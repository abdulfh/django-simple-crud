from rest_framework import serializers
from orders.models import Order
from cars.serializers import CarSerializers

class OrderSerializers(serializers.ModelSerializer):
    carId = CarSerializers(many=False)
    class Meta:
        model = Order
        fields = '__all__'

class OrderUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'