from django.urls import path
from save import views

urlpatterns = [
    path("saved/", views.SaveListView.as_view()),
    path("saved/<int:pk>/", views.SavedDetail.as_view()),
]
