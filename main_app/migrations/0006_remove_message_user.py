# Generated by Django 3.2.7 on 2021-09-09 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]