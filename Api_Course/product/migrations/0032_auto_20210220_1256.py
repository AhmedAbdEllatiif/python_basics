# Generated by Django 3.1.6 on 2021-02-20 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0031_auto_20210220_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 20, 12, 56, 35, 737011)),
        ),
    ]
