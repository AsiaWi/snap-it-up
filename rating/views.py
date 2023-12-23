from .models import Rating
from .serializers import RatingSerializer
from rest_framework import generics, permissions
from snap_it_up.permissions import IsOwnerOrReadOnly


class RatingList(generics.ListCreateAPIView):
    '''
    View Rating list and create rating only if authorised
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

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