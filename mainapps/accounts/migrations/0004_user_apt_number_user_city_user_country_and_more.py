# Generated by Django 5.0.4 on 2024-05-13 19:30

import django.core.validators
import mainapps.accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_blacklistedtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='apt_number',
            field=models.CharField(blank=True, help_text='Please enter your apartment number or house number.', max_length=200, null=True, verbose_name='Apartment Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, help_text='Please enter only alphabets.', max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Only alphabet characters are allowed.')], verbose_name='City'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, default='Nigeria', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='You must be above 18 years of age.', null=True, validators=[mainapps.accounts.models.adult_validator], verbose_name='Date Of Birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, help_text='Please enter only alphabets.', max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Only alphabet characters are allowed.')], verbose_name='State'),
        ),
        migrations.AddField(
            model_name='user',
            name='street_name',
            field=models.TextField(blank=True, help_text='Enter you Home Address.', null=True, verbose_name='Street Name'),
        ),
        migrations.AddField(
            model_name='user',
            name='street_number',
            field=models.CharField(blank=True, help_text='This field is optional. Please enter your street number.', max_length=200, null=True, verbose_name='Street Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(blank=True, help_text='Please enter a 6 digit zip code.', max_length=6, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{6}$', 'The zip code should be of the form DDDDDD.')], verbose_name='Zip Code'),
        ),
    ]
