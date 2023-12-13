from .serializers import AdvertSerializer
from .models import Advert
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from snap_it_up.permissions import IsOwnerOrReadOnly


class AdvertsList(generics.ListCreateAPIView):
    '''
    AdvertListCreate View provides GET method to provide a list 
    and allows to create a post with POST method
    '''
    serializer_class = AdvertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Advert.objects.all().order_by('-updated_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AdvertDetails(generics.RetrieveUpdateDestroyAPIView):
    '''
    Detail view for each Advert, get's an object based on pk
    checks permissions to allow access to update and delete or throws  an error
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def get_object(self):
        try:
            obj = self.get_queryset().get(pk=self.kwargs['pk'])
            self.check_object_permissions(self.request, obj)
            return obj
        except Advert.DoesNotExist:
            raise Http404("Profile does not exist")