# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('cache', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('dateTime', models.DateTimeField()),
                ('snippet', models.TextField()),
            ],
            options={
                'ordering': ['-dateTime'],
            },
        ),
    ]
