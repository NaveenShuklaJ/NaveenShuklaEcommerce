# Generated by Django 4.2.6 on 2023-10-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_remove_orders_address_remove_orderupdate_update_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
