# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('answer', models.TextField()),
                ('check', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('meaning', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='word',
            field=models.ForeignKey(related_name='question', to='word.Word'),
        ),
    ]
