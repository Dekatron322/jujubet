# Generated by Django 3.2.7 on 2021-09-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20210921_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='vipgames',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
