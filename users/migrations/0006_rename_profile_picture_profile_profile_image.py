# Generated by Django 4.0.2 on 2022-02-21 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_cover_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_picture',
            new_name='profile_image',
        ),
    ]
