from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    """
    User's profile adding more information for Django Auth User
    """
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    followers = models.ManyToManyField('self', through='Follow',
                                       through_fields=('followee', 'follower'),
                                       related_name='following', symmetrical=False)


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='follower')
    followee = models.ForeignKey(UserProfile, related_name='followee')
