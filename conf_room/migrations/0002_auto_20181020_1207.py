# Generated by Django 2.0.3 on 2018-10-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='air_conditioning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='tv',
            field=models.BooleanField(default=False),
        ),
    ]
