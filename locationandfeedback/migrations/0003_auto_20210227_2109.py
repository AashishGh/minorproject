# Generated by Django 3.1.1 on 2021-02-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationandfeedback', '0002_rateapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='group',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
