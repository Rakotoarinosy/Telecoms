# Generated by Django 4.2 on 2023-05-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0008_alter_acces_sim_libelle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type_sim',
            name='libelle',
            field=models.CharField(max_length=20, verbose_name='Type de SIM'),
        ),
    ]