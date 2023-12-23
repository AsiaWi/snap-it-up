from .models import Profile
from .serializers import ProfileSerializer
from snap_it_up.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.db.models import Count


class ProfileList(APIView):
    '''
    List all profiles, profile creation handled by django signals
    return number of adverts and number of ratings received by user
    '''

    def get(self, request):
        profiles = Profile.objects.annotate(
            advert_count=Count('owner__advert', distinct=True),
            rating_count=Count('owner__rated_user', distinct=True)
        )
        serializer = ProfileSerializer(profiles, many=True,
                                       context={'request': request})
        for profile in profiles:
            profile.average_rating = profile.calculate_average_rating()
        return Response(serializer.data)


class ProfileDetails(RetrieveUpdateAPIView):
    '''
    Retrieve and update profile, check permissions before each action taken
    PUT method allows to change location or profile picture only.
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
            advert_count=Count('owner__advert', distinct=True)
        )
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            obj = self.get_queryset().get(pk=self.kwargs['pk'])
            self.check_object_permissions(self.request, obj)
            return obj
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")
