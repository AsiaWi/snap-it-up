from django.db import models
from django.contrib.auth.models import User
from adverts.models import Advert


class Question(models.Model):
    '''
    Question model related to Advert and User, deleted on Advert/User deletion.
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    question_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.question_content
