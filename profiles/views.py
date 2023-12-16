from .models import Profile
from .serializers import ProfileSerializer
from snap_it_up.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class ProfileList(APIView):
    '''
    List all profiles, profile creation handled by django signals 
    '''
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileDetails(RetrieveUpdateAPIView):
    '''
    Retrieve and update profile, check permissions before each action taken
    '''
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