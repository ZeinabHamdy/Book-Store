# Generated by Django 5.1.2 on 2024-11-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='discount_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='no title', max_length=150),
        ),
    ]