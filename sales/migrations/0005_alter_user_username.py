# Generated by Django 5.1.2 on 2024-11-20 19:10

import sales.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[sales.models.validateUsername]),
        ),
    ]
