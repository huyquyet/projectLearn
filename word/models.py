from django.db import models


# Create your models here.

class Language(models.Model):
    name = models.TextField(default='English')

    def __unicode__(self):
        return self.name


class Word(models.Model):
    name = models.TextField()
    meaning = models.TextField()
    language = models.ForeignKey(Language, related_name='word')

    def __unicode__(self):
        return self.name


class Question(models.Model):
    word = models.ForeignKey(Word, related_name='question')
    answer = models.TextField()
    check = models.BooleanField()
