# Generated by Django 3.2.7 on 2021-09-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vipgames',
            name='league',
            field=models.CharField(choices=[('UEFA Champions League', 'UEFA Champions League'), ('LUEFA Europa League', 'UEFA Europa League'), ('La Liga', 'La Liga'), ('Serie A', 'Serie A'), ('Bundesliga', 'Bundesliga'), ('Ligue 1', 'Ligue 1'), ('FIFA Club World Cup', 'FIFA Club World Cup'), ('Copa del Rey', 'Copa del Rey'), ('Portuguese Liga', 'Portuguese Liga'), ('Dutch Eredivisie', 'Dutch Eredivisie'), ('Brasileiro Série A', 'Brasileiro Série A'), ('Mexican Primera Division Torneo Apertura', 'Mexican Primera Division Torneo Apertura'), ('Russian Premier Liga', 'Russian Premier Liga'), ('English League Championship', 'English League Championship'), ('Belgian Jupiler League', 'Belgian Jupiler League'), ('Austrian T-Mobile Bundesliga', ' Austrian T-Mobile Bundesliga'), ('Major League Soccer', 'Major League Soccer'), ('Turkish Turkcell Super Lig', 'Turkish Turkcell Super Lig'), ('Danish SAS-Ligaen', 'Danish SAS-Ligaen'), ('Swiss Raiffeisen Super League', 'Swiss Raiffeisen Super League'), ('Scottish Premiership', 'Scottish Premiership'), ('Argentina Primera Division', 'Argentina Primera Division'), ('German 2. Bundesliga', 'German 2. Bundesliga'), (' Greek Super League', ' Greek Super League'), ('Japanese J League', 'Japanese J League'), ('Norwegian Tippeligaen', 'Norwegian Tippeligaen'), ('Italy Serie B', 'Italy Serie B'), ('Spanish Segunda Division', 'Spanish Segunda Division'), ('French Ligue 2', 'French Ligue 2'), ('Swedish Allsvenskan', 'Swedish Allsvenskan'), ('Chinese Super League', 'Chinese Super League'), ('Australian A-League', 'Australian A-League'), ('English League One', ' English League One'), ('United Soccer League', 'United Soccer League'), ('South African ABSA Premier League', 'South African ABSA Premier League'), ('English League Two', 'English League Two'), ('Other', 'Other')], default='UEFA Champions League', max_length=1000),
        ),
    ]
