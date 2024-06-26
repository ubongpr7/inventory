# Generated by Django 4.2.13 on 2024-06-01 11:49

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_rename_type_typeof'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeof',
            options={'ordering': ['name'], 'verbose_name_plural': 'Types of Instances'},
        ),
        migrations.AddField(
            model_name='country',
            name='name',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
