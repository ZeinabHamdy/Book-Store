# Generated by Django 5.1.2 on 2024-11-20 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_alter_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]