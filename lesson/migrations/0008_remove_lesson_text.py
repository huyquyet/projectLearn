# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0007_lesson_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='text',
        ),
    ]
