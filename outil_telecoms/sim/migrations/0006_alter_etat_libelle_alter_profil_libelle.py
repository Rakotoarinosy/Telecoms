# Generated by Django 4.2 on 2023-05-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0005_alter_suivi_consommation_mois'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etat',
            name='libelle',
            field=models.CharField(max_length=30, verbose_name='Etat'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='libelle',
            field=models.CharField(max_length=40, verbose_name='Profil'),
        ),
    ]