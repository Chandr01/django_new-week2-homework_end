# Generated by Django 2.0 on 2017-12-06 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0004_coach_user2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='user2',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='coaches.User2'),
        ),
    ]
