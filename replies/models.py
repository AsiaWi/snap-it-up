from django.db import models
from django.contrib.auth.models import User
from questions.models import Question

class Reply(models.Model):
    '''
    Reply model related to AQuestion and User, deleted on Question/User deletion.
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reply_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.reply_content