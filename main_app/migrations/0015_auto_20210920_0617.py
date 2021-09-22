# Generated by Django 3.2.7 on 2021-09-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_vipgames_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='vipgames',
            name='dA_away_team',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dA_home_team',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dA_league',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dA_odds',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dA_result',
            field=models.CharField(choices=[('WON', 'WON'), ('LOST', 'LOST'), ('PENDING', 'PENDING')], default='PENDING', max_length=30),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dA_tip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dB_away_team',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dB_home_team',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dB_league',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dB_odds',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dB_result',
            field=models.CharField(choices=[('WON', 'WON'), ('LOST', 'LOST'), ('PENDING', 'PENDING')], default='PENDING', max_length=30),
        ),
        migrations.AddField(
            model_name='vipgames',
            name='dB_tip',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
