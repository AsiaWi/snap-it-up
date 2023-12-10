from django.shortcuts import render
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer

class ProfileList(APIView):
    '''
    List all profiles, profile creation handled by django signals 
    '''
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)