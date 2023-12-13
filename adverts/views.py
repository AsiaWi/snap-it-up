from .serializers import AdvertSerializer
from .models import Advert
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions, generics


class AdvertsList(generics.ListCreateAPIView):
    '''
    AdvertListCreate View provides GET method to provide a list and POST method.
    '''
    serializer_class = AdvertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Advert.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(advert_owner=self.request.user)