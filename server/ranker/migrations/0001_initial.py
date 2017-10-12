# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=b'', max_length=100)),
                ('image', models.CharField(blank=True, default=b'', max_length=200)),
                ('description', models.CharField(blank=True, default=b'', max_length=200)),
                ('developer', models.CharField(blank=True, default=b'', max_length=100)),
                ('genre', models.CharField(blank=True, default=b'[]', max_length=200)),
                ('published', models.DateField(blank=True, default=b'')),
                ('rank', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'ordering': ('rank',),
            },
        ),
    ]
