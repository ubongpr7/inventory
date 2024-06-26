# Generated by Django 4.2.13 on 2024-05-23 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_created_by_company_is_owner_and_more'),
        ('accounts', '0005_remove_user_type_of_user_user_is_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='company.company'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_main_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_worker',
            field=models.BooleanField(default=False),
        ),
    ]
