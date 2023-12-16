from django.urls import path
from questions import views

urlpatterns = [
    path("questions/", views.QuestionListView.as_view()),
    path("questions/<int:pk>/", views.QuestionDetail.as_view()),
]