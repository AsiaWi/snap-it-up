from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
 
    owner = models.ForeignKey(User, related_name='rated_by', on_delete=models.CASCADE)
    rated_user = models.ForeignKey(User, related_name='rated_user', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'rated_user']

    def __str__(self):
        return f'{self.owner} {self.rating} for {self.rated_user}'