# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0006_lessonuser_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='text',
            field=models.BooleanField(default=True),
        ),
    ]
