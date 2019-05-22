# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Llama',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='First name and last name')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Llama',
                'verbose_name_plural': 'Llamas',
            },
        ),
    ]
