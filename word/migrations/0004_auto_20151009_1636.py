# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0003_word_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='language',
            field=models.ForeignKey(related_name='word', to='word.Language'),
        ),
    ]
