# Generated by Django 5.0.4 on 2024-05-17 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocklocation',
            name='custom_icon',
        ),
    ]
