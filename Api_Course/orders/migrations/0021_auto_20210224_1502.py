# Generated by Django 3.1.6 on 2021-02-24 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20210224_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='ordererd',
            new_name='ordered',
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 15, 2, 3, 524315)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 15, 2, 3, 523315)),
        ),
    ]
