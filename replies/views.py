from .models import Reply
from .serializers import ReplySerializer, ReplyDetailsSerializer
from rest_framework import generics, permissions
from snap_it_up.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class ReplyListView(generics.ListCreateAPIView):
    '''
    View reply list and create an answer only if authorised
    '''
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reply.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Detail view for each Reply, get's an object based on pk
    checks permissions to allow access to update and delete or throws an error
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Reply.objects.all()
    serializer_class = ReplyDetailsSerializer
