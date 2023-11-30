# user_profiles/serializers.py
from rest_framework import serializers
from .models import UserProfile

# serializers.py

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'about', 'areas_of_interest']

