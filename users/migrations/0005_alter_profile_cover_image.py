# Generated by Django 4.0.2 on 2022-02-19 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_profile_image_profile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(blank=True, default='profiles/covers/default.jpg', null=True, upload_to='profiles/covers'),
        ),
    ]
