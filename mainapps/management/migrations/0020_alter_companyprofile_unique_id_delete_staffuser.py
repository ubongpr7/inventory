# Generated by Django 4.2.13 on 2024-06-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_rename_company_staffuser_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_id',
            field=models.CharField(default='200966582644193', editable=False, max_length=15, unique=True),
        ),
        migrations.DeleteModel(
            name='StaffUser',
        ),
    ]
