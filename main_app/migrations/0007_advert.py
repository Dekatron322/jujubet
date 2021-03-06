# Generated by Django 3.2.7 on 2021-09-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_message_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('link', models.CharField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
    ]
