from .models import Rating
from .serializers import RatingSerializer
from rest_framework import generics, permissions
from snap_it_up.permissions import IsOwnerOrReadOnly



class RatingList(generics.ListCreateAPIView):
  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetails(generics.RetrieveDestroyAPIView):
 
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer