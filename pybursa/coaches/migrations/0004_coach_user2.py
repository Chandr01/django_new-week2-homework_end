# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_auto_20171115_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='user2',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='coaches.User2'),
        ),
    ]
