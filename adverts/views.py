from .serializers import AdvertSerializer
from .models import Advert
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from snap_it_up.permissions import IsOwnerOrReadOnly
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.db.models import Count


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

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
     ]

    search_fields = [
        'advert_title',
        'tags__name',
        'item_description'
     ]

    ordering_fields = [
         'price',
         'created_at',
    ]


class AdvertDetails(HitCountMixin, generics.RetrieveUpdateDestroyAPIView):
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
            raise Http404("Advert does not exist")

    def retrieve(self, request, *args, **kwargs):
        '''
        Use existing retrieve method
        Increment the hit count
        Add hit count to the existing response
        '''
        instance = self.get_object()
        response = super().retrieve(request, *args, **kwargs)
        hit_count = HitCount.objects.get_for_object(instance)
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        response.data['hit_count'] = hit_count_response

        return response
