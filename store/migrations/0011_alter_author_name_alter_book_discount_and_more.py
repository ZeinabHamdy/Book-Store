# Generated by Django 5.1.2 on 2024-11-20 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_author_name_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='images/book_images/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]