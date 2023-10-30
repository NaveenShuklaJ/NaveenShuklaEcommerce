# Generated by Django 3.2 on 2021-10-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='item_json',
        ),
        migrations.AddField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='', max_length=6000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(default='', max_length=111),
        ),
    ]
