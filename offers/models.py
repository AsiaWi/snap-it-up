from django.db import models
from django.contrib.auth.models import User
from adverts.models import Advert
from django.db.models.signals import pre_save
from django.dispatch import receiver


OFFER_STATUS = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]

class Offer(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name='offers_made', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='offers_received', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=OFFER_STATUS, default='PENDING')
    message = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.seller_id:
            self.seller = self.advert.owner
        super().save(*args, **kwargs)