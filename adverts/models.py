from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from djmoney.models.fields import MoneyField
from hitcount.models import HitCountMixin


PAYMENT_OPTIONS = [
    ('Cash or Paypal', 'Cash or Paypal'),
    ('Cash only', 'Cash only'),
    ('PayPal only', 'PayPal only')
    
]

SHIPPMENT_OPTIONS = [
    ('Collection or delivery', 'Collection or delivery'),
    ('Collection Only', 'Collection Only'),
    ('Delivery Only', 'Delivery Only')
    
]

CATEGORIES = [
    ('Clothing', 'Clothing'),
    ('Electronics', 'Electronics'),
    ('HomeDeco/Furniture', 'HomeDeco/Furniture'),
    ('Games', 'Games'),
    ('Books', 'Books'),
    ('Beauty/Personal Care', 'Beauty/Personal Care'),
    ('Home appliances', 'Home appliances'),
    ('Vintage', 'Vintage'),
    ('Baby', 'Baby'),
    ('Pets', 'Pets'),
    ('Sports', 'Sports'),
    ('Other', 'Other')
]


class Advert(models.Model, HitCountMixin):
    '''
    Advert model to create an advert post.
    Listed in descending order whichever date is most recent: created/updated
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_dets = models.CharField(max_length=150, blank=False)
    advert_title = models.CharField(max_length=50, blank=True)
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to='images/', default='../upload.png_t8qvp6')
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='GBP',
                       blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_description = models.TextField(blank=True)
    payment_options = models.CharField(max_length=20, choices=PAYMENT_OPTIONS,
                                       default='Cash or Paypal')
    shippment_options = models.CharField(max_length=50,
                                         choices=SHIPPMENT_OPTIONS,
                                         default='Collection or delivery')
    active = models.BooleanField(default=True)
    categories = models.CharField(max_length=100,
                                  choices=CATEGORIES,
                                  default='Clothing')
    location = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return f'{self.advert_title}'
