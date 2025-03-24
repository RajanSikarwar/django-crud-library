from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger(__name__)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            # Use the serializer to validate and create the user
            serializer = self.get_serializer(data=request.data)
            
            # Validate data
            serializer.is_valid(raise_exception=True)
            
            # Create user
            user = serializer.save()
            
            # Generate token
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'user_id': user.id,
                'email': user.email,
                'username': user.username,
                'token': token.key,
                'is_admin': user.is_admin
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            # Log the full error for server-side debugging
            logger.error(f"Registration error: {str(e)}")
            
            # Return a more informative error response
            return Response({
                'error': 'Registration failed',
                'details': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            
            # Validate input
            if not email or not password:
                return Response({
                    'error': 'Email and password are required'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Custom authentication for email
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key, 
                    'user_id': user.id, 
                    'is_admin': user.is_admin,
                    'username': user.username
                })
            
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            return Response({
                'error': 'Login failed',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            # Delete the token to logout
            request.auth.delete()
            return Response({
                "detail": "Successfully logged out."
            })
        except Exception as e:
            logger.error(f"Logout error: {str(e)}")
            return Response({
                'error': 'Logout failed',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)