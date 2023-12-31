from .models import Question
from .serializers import QuestionSerializer, QuestionDetailsSerializer
from rest_framework import generics, permissions
from snap_it_up.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class QuestionListView(generics.ListCreateAPIView):
    '''
    View questions list and create a question only if authorised
    '''
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['advert']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Detail view for each Question, get's an object based on pk
    checks permissions to allow access to update and delete or throws  an error
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    