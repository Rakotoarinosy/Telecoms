# Generated by Django 4.2 on 2023-05-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='libelle',
            field=models.CharField(default='TELECOM', max_length=30, verbose_name='Catégorie'),
        ),
    ]
