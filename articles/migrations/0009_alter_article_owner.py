# Generated by Django 4.0.2 on 2022-02-18 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_user'),
        ('articles', '0008_alter_article_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(default='Anonim', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]