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
        serializer = ProfileSerializer(profiles, many=True,  context={'request': request})
        return Response(serializer.data)


class ProfileDetails(RetrieveUpdateAPIView):
    '''
    Retrieve a profile object using it's pk and allow updates to the profile
    IsOwnerOrRead only method used to allow updates for profile owners only
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)