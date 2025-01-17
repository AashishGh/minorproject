# Generated by Django 3.1.1 on 2021-03-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0026_auto_20210303_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='citizenship_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='land_map_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='land_ownership_document_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
