# Generated by Django 3.0.8 on 2021-02-01 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210201_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_address_1',
            new_name='address_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_address_2',
            new_name='address_2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_amount',
            new_name='quantity',
        ),
    ]
