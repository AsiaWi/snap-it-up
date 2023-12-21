from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rating.models import Rating


class Profile(models.Model):
    '''
    Profile model to create a profile,
    create profile upon registration
    '''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='images/', default ='../default_profile_hqnms8')
    
    def calculate_average_rating(self):
        ratings = Rating.objects.filter(rated_user=self.owner)
        total_ratings = ratings.count()
        if total_ratings > 0:
            sum_of_ratings = sum([rating.rating for rating in ratings])
            return sum_of_ratings / total_ratings
        return 'No ratings for this profile yet.'
        
    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
