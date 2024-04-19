from rest_framework import serializers
from .models import User, UserPin

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Controls the fields returned
        fields = ['user_id', 'first_name', 'middle_name', 'last_name', 'created_at', 'email']

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Defines the fields to be stored in the DB
        fields = ['first_name', 'middle_name', 'last_name', 'email']
        extra_kwargs = {
            'extra': 'forbid'  # Forbid extra fields in requests
        }

class UserPinPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPin
        fields = ['user_id','pin']
