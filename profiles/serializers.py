from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    profile_owner = serializers.ReadOnlyField(source="profile_owner.username")
    
    class Meta:
        model = Profile
        fields = [
            'id', 'profile_owner', 'location','created_at', 'profile_image'
        ]