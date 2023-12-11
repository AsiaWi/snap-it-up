from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    profile_owner = serializers.ReadOnlyField(source="profile_owner.username")
    
    class Meta:
        model = Profile
        fields = '__all__'