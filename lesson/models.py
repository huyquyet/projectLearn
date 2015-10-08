from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from word.models import Word


class Course(models.Model):
    name = models.TextField()
    content = models.TextField()

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    name = models.TextField()
    content = models.TextField()
    course = models.ForeignKey(Course, related_name='lesson')
    user = models.ManyToManyField(User, through='LessonUser', related_name='lesson')
    word = models.ManyToManyField(Word, related_name='lesson')

    def __unicode__(self):
        return self.name


class LessonUser(models.Model):
    user = models.ForeignKey(User, related_name='lesson_user')
    lesson = models.ForeignKey(Lesson, related_name='lesson_user')
