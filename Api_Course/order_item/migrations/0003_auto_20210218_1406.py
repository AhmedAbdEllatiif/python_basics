# Generated by Django 3.1.6 on 2021-02-18 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_item', '0002_remove_orderitem_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product_id',
            new_name='product',
        ),
    ]