# Generated by Django 3.1.1 on 2021-03-02 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0021_auto_20210227_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image1',
            new_name='backsideview',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image2',
            new_name='frontview',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image3',
            new_name='leftsideview',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image4',
            new_name='rightsideview',
        ),
    ]
