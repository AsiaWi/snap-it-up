from django.urls import path
from offers import views

urlpatterns = [
    path("offers/", views.OfferCreate.as_view()),
    path("offers/<int:pk>/", views.OfferDetails.as_view()),
]