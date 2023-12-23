from django.db import models
from django.contrib.auth.models import User
from adverts.models import Advert


class Save(models.Model):
    """
    Save model,(related to user and advert) user can save an advert by
    clicking an icon
    List view enables user to easily access all saved adverts
    'unique_together' makes sure a user can't save the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-advert__updated_at']
        unique_together = ['owner', 'advert']

    def __str__(self):
        return f'{self.owner} {self.post}'
