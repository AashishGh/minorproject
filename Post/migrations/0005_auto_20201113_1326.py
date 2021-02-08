# Generated by Django 3.1.1 on 2020-11-13 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20201113_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='phone_number',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be 10 digits and  entered in the format: '98XXXXXXXX'.", regex='^\\+?1?\\d{10}$')]),
        ),
    ]