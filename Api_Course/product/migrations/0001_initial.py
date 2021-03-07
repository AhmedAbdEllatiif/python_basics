# Generated by Django 3.1.6 on 2021-02-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('rate', models.CharField(choices=[('5', 'EXCELLENT'), ('4', 'GREAT'), ('3', 'GOOD'), ('2', 'ACCEPTED'), ('1', 'POOR'), ('0', 'NOTRATED')], default='0', max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
