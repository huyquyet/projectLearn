from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Language(models.Model):
    name = models.TextField(default='English')

    def __unicode__(self):
        return self.pk


class Word(models.Model):
    name = models.TextField()
    meaning = models.TextField()
    description = models.TextField(default=None)
    language = models.ForeignKey(Language, related_name='word')
    user = models.ManyToManyField(User, related_name='word')

    def __unicode__(self):
        return self.name


class Question(models.Model):
    word = models.ForeignKey(Word, related_name='question')
    answer = models.TextField()
    check = models.BooleanField(help_text='Answer True or False')

