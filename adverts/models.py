from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from djmoney.models.fields import MoneyField
from hitcount.models import HitCountMixin


PAYMENT_OPTIONS = (
    ('cash', 'Cash'),
    ('PayPal', 'PayPal'),
    ('either', 'Cash or Paypal')
)

SHIPPMENT_OPTIONS = (
    ('collection', 'Collection Only'),
    ('postage', 'Royal Mail Only'),
    ('either', 'Collection or Royal Mail delivery')
)


class Advert(models.Model, HitCountMixin):
    '''
    Advert model to create an advert post.
    Listed in descending order whichever date is most recent: created/updated
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    advert_title = models.CharField(max_length=50, blank=True)
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to='images/', blank=False)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='GBP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_description = models.TextField(blank=False, null=False)
    payment_options = models.CharField(max_length=20, choices=PAYMENT_OPTIONS,
                               default='either')
    shippment_options = models.CharField(max_length=50, choices=SHIPPMENT_OPTIONS,
                               default='either')
    
    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return f'{self.advert_title}'