from rest_framework_simplejwt import authentication, tokens

class AuthenticatedMiddleware():
    WHITELISTED_URLS = [
        "/auth/login"
    ]
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in self.WHITELISTED_URLS:
            return None
        
        tokenString = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        accessToken = tokens.AccessToken(tokenString)
        request.user_id = accessToken.payload['user_id']
        request.is_admin = accessToken.payload['is_admin']