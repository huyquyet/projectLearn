# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_auto_20151009_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
