# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_lesson_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonuser',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
