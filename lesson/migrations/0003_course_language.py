# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0003_word_language'),
        ('lesson', '0002_lesson_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ForeignKey(to='word.Language', default='1', related_name='course'),
        ),
    ]
