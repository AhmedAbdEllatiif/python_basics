# Generated by Django 3.1.6 on 2021-02-28 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0043_auto_20210228_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 19, 11, 31, 580911)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 19, 11, 31, 580911)),
        ),
    ]
