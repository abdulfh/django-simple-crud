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

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in self.WHITELISTED_APP_NAME:
            return None
        
        tokenString = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        accessToken = tokens.AccessToken(tokenString)
        request.user_id = accessToken.payload['user_id']
        request.is_admin = accessToken.payload['is_admin']
        current_url = resolve(request.path_info).app_name
        
        print(current_url)
        if current_url in self.WHITELISTED_ADMIN_APP_NAME and request.is_admin != True:
            return JsonResponse({"errors":"Not Found"}, safe=False,status=status.HTTP_404_NOT_FOUND)
        