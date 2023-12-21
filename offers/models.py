from django.db import models
from django.contrib.auth.models import User
from adverts.models import Advert

OFFER_STATUS= [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]

class Offer(models.Model):
    '''
    Offer model allowing users to handle the sales.
    '''
    buyer = models.ForeignKey(User, related_name='offer_creator', on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=OFFER_STATUS, default='PENDING')
    message = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def seller(self):
        return self.advert.owner