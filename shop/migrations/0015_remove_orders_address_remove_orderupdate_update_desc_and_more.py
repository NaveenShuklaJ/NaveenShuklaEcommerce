# Generated by Django 4.2.6 on 2023-10-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_orders_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orderupdate',
            name='update_desc',
        ),
        migrations.AddField(
            model_name='orderupdate',
            name='address',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='orderupdate',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AddField(
            model_name='orderupdate',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
