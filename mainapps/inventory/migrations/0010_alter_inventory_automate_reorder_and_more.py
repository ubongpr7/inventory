# Generated by Django 4.2.13 on 2024-06-14 09:37

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_delete_country'),
        ('inventory', '0009_inventory_automate_reorder_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='automate_reorder',
            field=models.BooleanField(default=False, help_text='If product reaches reoder point, do you want an automated reorder processing '),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='expiration_policy',
            field=models.CharField(choices=[('0', 'Dispose of stock'), ('1', 'Return to manufacturer')], default='0', help_text='What happens if product expires', max_length=200),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='i_type',
            field=models.ForeignKey(limit_choices_to={'which_model': 'inventory'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.typeof', verbose_name='Type of  inventory*'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='minimum_stock_level',
            field=models.IntegerField(default=0, help_text='Minimum stock level before you receive alert'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Inventory name*'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='re_order_point',
            field=models.IntegerField(default=10, help_text='At what point can reorder activities be triggered '),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='recall_policy',
            field=models.CharField(choices=[('0', 'Remove from stock'), ('1', 'Notify customers'), ('3', 'Replace item'), ('4', 'Destroy item'), ('5', 'Repair item')], default='0', help_text='What happens if product is bad', max_length=200),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='unit',
            field=models.ForeignKey(blank=True, help_text='Set unit for items in this inventory e.g pieces,cm,m...', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventories', to='common.unit', verbose_name='Unit of measurement'),
        ),
        migrations.AlterField(
            model_name='inventorycategory',
            name='name',
            field=models.CharField(help_text='It must be unique', max_length=200, unique=True, verbose_name='Category name*'),
        ),
        migrations.AlterField(
            model_name='inventorycategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='Parent  to which this category falls', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='inventory.inventorycategory', verbose_name='Parent category'),
        ),
    ]
