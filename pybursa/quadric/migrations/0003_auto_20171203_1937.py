# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadric', '0002_auto_20171121_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quadric_logik',
            name='packag',
            field=models.CharField(choices=[('standart', 'Standart'), ('gold', 'Gold'), ('vip', 'VIP')], default='gold', max_length=100),
        ),
    ]
