# Generated by Django 3.0.1 on 2021-02-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0014_auto_20210210_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='breadth',
            new_name='Area',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='phone_number',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='url_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Name',
            new_name='owners_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='post',
            name='payment_verification_slip',
            field=models.CharField(choices=[('E-Sewa', 'E-Sewa'), ('Khalti', 'Khalti')], default='Khalti', max_length=20),
        ),
    ]
