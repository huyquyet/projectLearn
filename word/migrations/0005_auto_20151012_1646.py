# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0004_auto_20151009_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='check',
            field=models.BooleanField(help_text='Answer True or False'),
        ),
    ]
