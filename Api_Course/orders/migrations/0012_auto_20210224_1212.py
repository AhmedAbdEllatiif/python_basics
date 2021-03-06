# Generated by Django 3.1.6 on 2021-02-24 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20210224_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 12, 12, 45, 206493)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 12, 12, 45, 204494)),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.CharField(choices=[(5, 'Excellent'), (4, 'Great'), (3, 'Good'), (2, 'Accepted'), (1, 'Poor'), (0, 'Notrated')], default=0, max_length=12),
        ),
    ]
