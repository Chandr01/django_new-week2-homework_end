# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=2000)),
                ('from_email', models.CharField(max_length=255)),
                ('create_date', models.CharField(max_length=255)),
            ],
        ),
    ]
