# Generated by Django 5.0.4 on 2024-05-09 12:24

import django.core.validators
import django.db.models.deletion
import django.db.models.manager
import mainapps.common.custom_fields
import mainapps.utils.generators
import mainapps.utils.validators
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('inventory', '0001_initial'),
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockLocationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Brief name for the stock location type (unique)', max_length=100, unique=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, help_text='Longer form description of the stock location type (optional)', max_length=250, verbose_name='Description')),
                ('icon', models.CharField(blank=True, choices=[('icon1', 'Icon 1'), ('icon2', 'Icon 2')], help_text='Icon class for the default icon for locations that have no icon set (optional)', max_length=100, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Stock Location Type',
                'verbose_name_plural': 'Stock Location Types',
            },
        ),
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packaging', models.CharField(blank=True, help_text='Description of how the StockItem is packaged (e.g. "reel", "loose", "tape" etc)', max_length=50, null=True, verbose_name='Packaging')),
                ('serial', models.CharField(blank=True, help_text='Unique serial number for this StockItem', max_length=100, null=True, validators=[mainapps.utils.validators.validate_serial_number], verbose_name='Serial Number')),
                ('serial_int', models.IntegerField(default=0)),
                ('link', models.URLField(blank=True, help_text='Optional URL to link to an external resource', null=True, verbose_name='External Link')),
                ('batch', models.CharField(blank=True, default=mainapps.utils.generators.generate_batch_code, help_text='Batch code for this stock item', max_length=100, null=True, validators=[mainapps.utils.validators.validate_batch_code], verbose_name='Batch Code')),
                ('quantity', models.DecimalField(decimal_places=5, default=1, max_digits=15, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stock Quantity')),
                ('expiry_date', models.DateField(blank=True, help_text='Expiry date for stock item. Stock will be considered expired after this date', null=True, verbose_name='Expiry Date')),
                ('stocktake_date', models.DateField(blank=True, null=True)),
                ('review_needed', models.BooleanField(default=False)),
                ('delete_on_deplete', models.BooleanField(default=False, help_text='Delete this Stock Item when stock is depleted', verbose_name='Delete on deplete')),
                ('status', models.PositiveIntegerField(choices=[(10, 'OK'), (50, 'Attention needed'), (55, 'Damaged'), (60, 'Destroyed'), (65, 'Rejected'), (70, 'Lost'), (75, 'Quarantined'), (85, 'Returned')], default=10, help_text='Status of this StockItem (ref: InvenTree.status_codes.StockStatus)', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Status')),
                ('purchase_price', mainapps.common.custom_fields.MoneyField(blank=True, decimal_places=2, help_text='Single unit purchase price at the time of purchase', max_digits=19, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Purchase Price')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('belongs_to', models.ForeignKey(blank=True, help_text='Is this item installed in another item?', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='installed_parts', to='stock.stockitem', verbose_name='Installed In')),
                ('customer', models.ForeignKey(blank=True, help_text='Customer', limit_choices_to={'is_customer': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_stock', to='company.company', verbose_name='Customer')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Link to another StockItem from which this StockItem was created', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='stock.stockitem', verbose_name='Parent Stock Item')),
                ('purchase_order', models.ForeignKey(blank=True, help_text='Link to a PurchaseOrder (if this stock item was created from a PurchaseOrder)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_items', to='orders.purchaseorder', verbose_name='Source Purchase Order')),
                ('sales_order', models.ForeignKey(blank=True, help_text='Link   item to a SalesOrder', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_items', to='orders.salesorder', verbose_name='Destination Sales Order')),
                ('stocktaker', models.ForeignKey(blank=True, help_text='User that performed the most recent stocktake', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stocktakes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Stock Item',
                'verbose_name_plural': 'Stock Items',
            },
        ),
        migrations.CreateModel(
            name='StockItemTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_type', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.CharField(blank=True, help_text='Entry notes', max_length=512, null=True, verbose_name='Notes')),
                ('deltas', models.JSONField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracking_info', to='stock.stockitem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tracked_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_icon', models.CharField(blank=True, db_column='icon', help_text='Icon (optional)', max_length=100, null=True, verbose_name='Icon')),
                ('structural', models.BooleanField(default=False, help_text='Stock items may not be directly located into a structural stock location, but may be located to child locations.', verbose_name='Structural')),
                ('external', models.BooleanField(default=False, help_text='This is an external stock location', verbose_name='External')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('official', models.ForeignKey(blank=True, help_text='Select the manager for this stock location', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_locations', to=settings.AUTH_USER_MODEL, verbose_name='Manager')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Parent category, if any.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='stock.stocklocation', verbose_name='Parent Category')),
                ('location_type', models.ForeignKey(blank=True, help_text='Stock location type of this location', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_locations', to='stock.stocklocationtype', verbose_name='Location type')),
            ],
            options={
                'verbose_name': 'Stock Location',
                'verbose_name_plural': 'Stock Locations',
            },
            managers=[
                ('_tree_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='stockitem',
            name='location',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='Where this StockItem is located', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_items', to='stock.stocklocation', verbose_name='Stock Location'),
        ),
    ]