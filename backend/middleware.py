from rest_framework_simplejwt import tokens
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.urls import resolve

class AuthenticatedMiddleware():
    WHITELISTED_APP_NAME = [
        "auth"
    ]
    
    WHITELISTED_ADMIN_APP_NAME = [
        "cars"
    ]

    WHITELISTED_USER_ROUTE = [
        "cars/list"
    ]
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        current_url = resolve(request.path_info).app_name
        current_route = resolve(request.path_info).route

        if current_url in self.WHITELISTED_APP_NAME:
            return None
        
        tokenString = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        accessToken = tokens.AccessToken(tokenString)
        request.user_id = accessToken.payload['user_id']
        request.is_admin = accessToken.payload['is_admin']
        

        if current_route in self.WHITELISTED_USER_ROUTE and request.is_admin != True:
            return None
        
        if current_url in self.WHITELISTED_ADMIN_APP_NAME and request.is_admin != True:
            return JsonResponse({"errors":"Not Found"}, safe=False,status=status.HTTP_404_NOT_FOUND)
        