from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    '''
    Rating model allows for user to rate another user.
    Star rating and feedback can be left.
    Profiles can be rated many times
    '''
    owner = models.ForeignKey(User, related_name='rated_by',
                              on_delete=models.CASCADE)
    rated_user = models.ForeignKey(User, related_name='rated_user',
                                   on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=(
                                         (1, '1 star'),
                                         (2, '2 stars'),
                                         (3, '3 stars'),
                                         (4, '4 stars'),
                                         (5, '5 stars')
                                         ))
    feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_rating(self, new_rating_value):
        self.rating = new_rating_value
        self.save()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} rated {self.rating} for {self.rated_user}'
