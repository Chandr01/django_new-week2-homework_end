# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20171114_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='courses',
            field=models.ManyToManyField(null=True, to='course.Course'),
        ),
    ]
