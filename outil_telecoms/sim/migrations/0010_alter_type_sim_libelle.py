# Generated by Django 4.2 on 2023-05-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0009_alter_type_sim_libelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type_sim',
            name='libelle',
            field=models.CharField(max_length=20, unique=True, verbose_name='Type de SIM'),
        ),
    ]
