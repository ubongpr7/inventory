# Generated by Django 4.2.13 on 2024-06-14 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0023_alter_companyprofile_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_id',
            field=models.CharField(default='279245889834363', editable=False, max_length=15, unique=True),
        ),
    ]
