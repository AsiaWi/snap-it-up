from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Advert, Offer
from .serializers import OfferSerializer, OfferListSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from django_filters.rest_framework import DjangoFilterBackend


class OfferCreate(generics.ListCreateAPIView):
    '''
    Offer ListCreate view provides GET and POST methods
    to allow for listing all offers and creating an offer.
    Permissions checked- available for auth users only
    '''
    queryset = Offer.objects.all()
    serializer_class = OfferListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['advert']

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

class OfferDetails(generics.RetrieveUpdateAPIView):
    '''
    Offer detail view, permissions to view only by
    a seller if logged in.
    PUT method checks if offer status is 'SOLD'
    if so- advert active status sets to false.
    Once offer accepted users can still exchange messages
    however unable to change the status.
    '''
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        if user != obj.seller:
            raise PermissionDenied(
                  "You do not have permission to manage this offer.")
        return obj

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == 'SOLD':
            return Response({
                'message': 'The offer has already been accepted and the advert deactivated.'
                }, status=status.HTTP_400_BAD_REQUEST)
       
        old_status = instance.status
        serializer = self.get_serializer(instance,
                                         data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
      
        new_status = serializer.validated_data.get('status')

        if old_status != 'SOLD' and new_status == 'SOLD':
            instance.advert.active = False
            instance.advert.save()
            return Response({
                 'message': 'Offer accepted and advert deactivated.'},
                  status=status.HTTP_200_OK)
      
        elif old_status == 'SOLD' and new_status != 'SOLD':
            raise MethodNotAllowed(method=request.method)
            

        return Response(serializer.data)
