from .models import Rating
from .serializers import RatingSerializer
from rest_framework import generics, permissions
from snap_it_up.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class RatingList(generics.ListCreateAPIView):
    '''
    View Rating list and create rating only if authorised
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rated_user']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetails(generics.RetrieveUpdateDestroyAPIView):
    '''
    Detail view for each Rating, get's an object based on pk
    checks permissions to allow access to update and delete or throws an error
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer