# Generated by Django 3.1.6 on 2021-02-18 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20210218_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 18, 15, 48, 25, 910780)),
        ),
    ]
