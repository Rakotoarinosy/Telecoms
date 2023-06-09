# Generated by Django 4.2 on 2023-06-06 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0008_alter_sortie_numsortie_mouvement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mouvement',
            name='inactif',
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='affecte',
            field=models.IntegerField(default=0, verbose_name='Quantité affectée'),
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='article_modele',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipement.article_modele'),
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='disponible',
            field=models.IntegerField(default=0, verbose_name='Quantité disponible'),
        ),
    ]
