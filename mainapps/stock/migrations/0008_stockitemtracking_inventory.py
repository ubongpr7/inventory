# Generated by Django 4.2.13 on 2024-06-14 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_alter_inventory_automate_reorder_and_more'),
        ('stock', '0007_remove_stockitem_category_delete_stockcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitemtracking',
            name='inventory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.inventory'),
        ),
    ]