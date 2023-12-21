from .models import Offer, Advert
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import OfferSerializer
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

class OffersList(generics.ListCreateAPIView):
    '''
    View Offers list 
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)


class OfferDetails(generics.RetrieveUpdateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user

        if user not in [obj.buyer, obj.seller]:
            raise PermissionDenied("You do not have permission to perform this action.")

        return obj

    def perform_update(self, serializer):
        instance = self.get_object()
        serializer.save()

        if instance.status == 'ACCEPTED':
            instance.advert.active = False
            instance.advert.save()

        return Response({'message': 'Offer accepted and advert deactivated.'}, status=status.HTTP_200_OK)