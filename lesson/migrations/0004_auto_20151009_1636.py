# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_course_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.ForeignKey(related_name='course', to='word.Language'),
        ),
    ]
