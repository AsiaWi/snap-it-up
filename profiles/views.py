from .models import Profile
from .serializers import ProfileSerializer
from snap_it_up.permissions import IsOwnerOrReadOnly
from rest_framework import generics, filters
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.db.models import Count, Case, When, Value, FloatField, Sum, F


class ProfileList(generics.ListAPIView):
    '''
    List all profiles, profile creation handled by django signals
    return number of adverts and number of ratings received by user
    Average rating here, for ordering purposes only,
    averate_rating in detail view is
    more precise to display on users profile.
    '''
    queryset = Profile.objects.annotate(
        advert_count=Count('owner__advert', distinct=True),
        rating_count=Count('owner__rated_user', distinct=True),
        total_ratings=Sum('owner__rated_user__rating'),
        average_rating=Case(
            When(rating_count__gt=0, then=F('total_ratings') /
                 F('rating_count')), default=Value(0),))

    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ["-average_rating"]


class ProfileDetails(RetrieveUpdateAPIView):
    '''
    Retrieve and update profile, check permissions before each action taken
    PUT method allows to change location or profile picture only.
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            obj = Profile.objects.annotate(
                advert_count=Count('owner__advert', distinct=True),
                rating_count=Count('owner__rated_user', distinct=True)
            ).get(pk=self.kwargs['pk'])
            self.check_object_permissions(self.request, obj)
            obj.average_rating = obj.calculate_average_rating()
            return obj
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")
