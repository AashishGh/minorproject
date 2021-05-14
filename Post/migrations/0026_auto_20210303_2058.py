# Generated by Django 3.1.1 on 2021-03-03 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0025_auto_20210303_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='citizenship_photo',
            field=models.ImageField(blank=True, default=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='land_map_photo',
            field=models.ImageField(blank=True, default=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='land_ownership_document_photo',
            field=models.ImageField(blank=True, default=True, null=True, upload_to='images/'),
        ),
    ]