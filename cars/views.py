from django.http import JsonResponse
from cars.models import Car
from cars.serializers import CarSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def list_car(request):
    cars = Car.objects.all()
    serializer = CarSerializers(cars, many=True)
    return JsonResponse({"cars" : serializer.data}, safe=False)

@api_view(['POST'])
def store_car(request):
    serializer = CarSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_car(request, id):
    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarSerializers(car)
    return JsonResponse(serializer.data)

@api_view(['PUT'])
def update_car(request, id):
    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarSerializers(car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_car(request, id):
    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    