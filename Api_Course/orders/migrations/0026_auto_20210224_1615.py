# Generated by Django 3.1.6 on 2021-02-24 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20210224_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_num',
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 16, 15, 2, 849464)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 16, 15, 2, 849464)),
        ),
    ]
