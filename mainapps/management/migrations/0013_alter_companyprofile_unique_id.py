# Generated by Django 4.2.13 on 2024-06-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_alter_companyprofile_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_id',
            field=models.CharField(default='334236680707761', editable=False, max_length=15, unique=True),
        ),
    ]
