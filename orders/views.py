from django.http import JsonResponse
from orders.models import Order
from orders.serializers import OrderSerializers, OrderUpdateSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def list_order(request):
    orders = filterList(request)
    orders.prefetch_related('car')
    serializer = OrderSerializers(orders, many=True)
    return JsonResponse({"orders" : serializer.data}, safe=False)

@api_view(['POST'])
def store_order(request):
    buildRequest = requestBuilder(request)
    serializer = OrderSerializers(data=buildRequest.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_order(request, id):
    try:
        order = filterDetail(request, id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = OrderSerializers(order)
    return JsonResponse(serializer.data)

@api_view(['PUT'])
def update_order(request, id):
    try:
        order = filterDetail(request, id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = OrderUpdateSerializers(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_order(request, id):
    try:
        order = filterDetail(request, id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def responseBuild(response):
    for list in response:
        print(list.carid)

def filterList(request):
    order = Order.objects.all()
    if request.is_admin:
        return order
    
    return order.filter(userId=request.user_id).values()

def filterDetail(request, id):
    order = Order.objects.all()
    if request.is_admin:
        return order.get(pk=id)
    
    return order.filter(id=id, userId=request.user_id).get()