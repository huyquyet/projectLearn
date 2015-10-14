# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('word', '0006_word_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='user',
            field=models.ManyToManyField(related_name='word', to=settings.AUTH_USER_MODEL),
        ),
    ]
