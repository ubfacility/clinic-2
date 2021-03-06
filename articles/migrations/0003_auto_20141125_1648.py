# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20141125_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
