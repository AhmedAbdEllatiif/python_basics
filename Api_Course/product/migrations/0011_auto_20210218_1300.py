# Generated by Django 3.1.6 on 2021-02-18 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210218_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 18, 13, 0, 40, 951602)),
        ),
    ]
