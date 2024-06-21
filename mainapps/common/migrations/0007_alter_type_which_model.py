# Generated by Django 4.2.13 on 2024-05-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_type_type_unique_type_name_which_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='which_model',
            field=models.CharField(choices=[('inventory', 'Inventory'), ('stock_item', 'Stock item'), ('company', 'Company'), ('policy', 'Policy'), ('industry', 'Industry')], max_length=30),
        ),
    ]