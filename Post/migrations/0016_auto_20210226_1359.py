# Generated by Django 3.0.1 on 2021-02-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0015_auto_20210226_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='payment_completed',
        ),
        migrations.AlterField(
            model_name='post',
            name='payment_verification_slip',
            field=models.ImageField(default='True', upload_to='images/'),
        ),
    ]