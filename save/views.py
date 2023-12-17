from .models import Save
from .serializers import SaveSerializer
from rest_framework import generics, permissions
from snap_it_up.permissions import IsOwnerOrReadOnly

class SaveListView(generics.ListCreateAPIView):
    '''
    View saved adverts list
    Add to saved adverts for authorised users
    '''
    serializer_class = SaveSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SavedDetail(generics.RetrieveDestroyAPIView):
    '''
    Retrieve a saved item by id
    Delete save to remove from saved items
    permissions checked for not authorised access
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    
