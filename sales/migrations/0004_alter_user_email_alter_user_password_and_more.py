# Generated by Django 5.1.2 on 2024-11-20 19:08

import sales.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[sales.models.validatePassword]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='no name', max_length=50, unique=True, validators=[sales.models.validateUsername]),
        ),
    ]