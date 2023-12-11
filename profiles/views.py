from django.shortcuts import render
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from django.http import Http404
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Checks if user is a profile owner if not allows access to read-only
    '''
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.profile_owner == request.user


class ProfileList(APIView):
    '''
    List all profiles, profile creation handled by django signals 
    '''
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetails(RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            obj = self.get_queryset().get(pk=self.kwargs['pk'])
            self.check_object_permissions(self.request, obj)
            return obj
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")