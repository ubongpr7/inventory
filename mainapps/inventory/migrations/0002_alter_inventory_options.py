# Generated by Django 4.2.13 on 2024-05-22 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Inventories'},
        ),
    ]
