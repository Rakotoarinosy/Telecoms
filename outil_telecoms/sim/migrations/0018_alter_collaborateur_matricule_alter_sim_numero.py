# Generated by Django 4.2 on 2023-05-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0017_alter_affectation_sim_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborateur',
            name='matricule',
            field=models.CharField(unique=True, verbose_name='Matricule'),
        ),
        migrations.AlterField(
            model_name='sim',
            name='numero',
            field=models.IntegerField(verbose_name='Numéro Téléphone'),
        ),
    ]
