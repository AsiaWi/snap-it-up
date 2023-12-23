from django.urls import path, include
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', views.ProfileDetails.as_view()),
]
