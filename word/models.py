from django.db import models


# Create your models here.

class Word(models.Model):
    name = models.TextField()
    meaning = models.TextField()

    def __unicode__(self):
        return self.name


class Question(models.Model):
    word = models.ForeignKey(Word, related_name='question')
    answer = models.TextField()
    check = models.BooleanField()