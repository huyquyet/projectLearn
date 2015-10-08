from django.utils import timezone
from django.db import models

# Create your models here.
from lesson.models import LessonUser
from word.models import Question


class Exam(models.Model):
    lesson_user = models.ForeignKey(LessonUser, related_name='exam')
    date = models.DateTimeField(default=timezone.now)


class Answer(models.Model):
    exam = models.ForeignKey(Exam, related_name='answer')
    question = models.ForeignKey(Question, related_name='answers')
