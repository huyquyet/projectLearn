# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='language',
            field=models.ForeignKey(to='word.Language', default='1', related_name='word'),
        ),
    ]
