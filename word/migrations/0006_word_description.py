# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0005_auto_20151012_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
