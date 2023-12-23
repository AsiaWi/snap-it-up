from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Advert, Offer
from .serializers import OfferSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed


class OfferCreate(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)


class OfferDetails(generics.RetrieveUpdateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        if user != obj.buyer and user != obj.seller:
            raise PermissionDenied(
                  "You do not have permission to access this offer.")
        return obj

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        old_status = instance.status
        serializer = self.get_serializer(instance,
                                         data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        new_status = serializer.validated_data.get('status')

        if old_status != 'ACCEPTED' and new_status == 'ACCEPTED':
            instance.advert.active = False
            instance.advert.save()
            return Response({
                 'message': 'Offer accepted and advert deactivated.'},
                  status=status.HTTP_200_OK)
        elif old_status == 'ACCEPTED' and new_status != 'ACCEPTED':
            raise MethodNotAllowed(method=request.method)

        return Response(serializer.data)
