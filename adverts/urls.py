from django.urls import path
from adverts import views

urlpatterns = [
    path('adverts/', views.AdvertsList.as_view()),
    path('adverts/<int:pk>/', views.AdvertDetails.as_view()),
]
