# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('content', models.TextField()),
                ('course', models.ForeignKey(related_name='lesson', to='lesson.Course')),
            ],
        ),
        migrations.CreateModel(
            name='LessonUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('lesson', models.ForeignKey(related_name='lesson_user', to='lesson.Lesson')),
                ('user', models.ForeignKey(related_name='lesson_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='user',
            field=models.ManyToManyField(related_name='lesson', through='lesson.LessonUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lesson',
            name='word',
            field=models.ManyToManyField(related_name='lesson', to='word.Word'),
        ),
    ]
