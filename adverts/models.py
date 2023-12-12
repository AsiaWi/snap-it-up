from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from djmoney.models.fields import MoneyField
from hitcount.models import HitCountMixin, HitCount


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
    advert_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    advert_title = models.CharField(max_length=50, blank=True )
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to='images/', blank=False)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='GBP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    item_description = models.TextField(blank=False, null=False)
    payment_options = models.CharField(max_length=20, choices=PAYMENT_OPTIONS,
                               default='either')
    shippment_options = models.CharField(max_length=50, choices=SHIPPMENT_OPTIONS,
                               default='either')
    hit_count_generic = models.OneToOneField(HitCount,on_delete=models.CASCADE, related_query_name='hit_count_generic_relation')

    def clean(self):
        if not self.advert_title and not self.tags:
            raise ValidationError('At least one of the fields: advert title or tags must be provided')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.advert_title}'