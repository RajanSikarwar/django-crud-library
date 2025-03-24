from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    is_admin = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_admin']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True}
        }

    def create(self, validated_data):
        # Extract is_admin, defaulting to False if not provided
        is_admin = validated_data.pop('is_admin', False)
        
        # Create user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_admin=is_admin
        )
        return user