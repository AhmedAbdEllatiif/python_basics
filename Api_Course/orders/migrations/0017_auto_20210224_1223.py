# Generated by Django 3.1.6 on 2021-02-24 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20210224_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 12, 23, 33, 636906)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 12, 23, 33, 636906)),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.IntegerField(choices=[(5, 'Excellent'), (4, 'Great'), (3, 'Good'), (2, 'Accepted'), (1, 'Poor'), (0, 'Notrated')], default=0),
        ),
    ]
