# Generated by Django 3.2.7 on 2021-09-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_vipgames_league'),
    ]

    operations = [
        migrations.AddField(
            model_name='vipgames',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]