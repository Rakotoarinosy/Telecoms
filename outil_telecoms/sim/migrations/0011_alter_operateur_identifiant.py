# Generated by Django 4.2 on 2023-05-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0010_alter_type_sim_libelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operateur',
            name='identifiant',
            field=models.CharField(max_length=20, verbose_name='Identifiant'),
        ),
    ]
