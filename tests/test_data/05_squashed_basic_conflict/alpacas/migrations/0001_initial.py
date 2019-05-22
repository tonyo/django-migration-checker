# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('llamas', '0002_new_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alpaca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('some_attr', models.BooleanField(default=False, verbose_name='Nothing really')),
            ],
            bases=(models.Model,),
        ),
    ]
