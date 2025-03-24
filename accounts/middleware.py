# Handles token authentication
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class TokenAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Token '):
            token_key = auth_header.split(' ')[1]
            try:
                token = Token.objects.get(key=token_key)
                request.user = token.user
            except Token.DoesNotExist:
                pass