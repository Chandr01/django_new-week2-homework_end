# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20171115_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vare', models.CharField(max_length=100)),
            ],
        ),
    ]
