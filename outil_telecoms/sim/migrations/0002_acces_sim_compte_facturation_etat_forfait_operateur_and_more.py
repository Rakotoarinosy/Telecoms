# Generated by Django 4.2 on 2023-05-02 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acces_sim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20, verbose_name='Acces')),
            ],
        ),
        migrations.CreateModel(
            name='Compte_facturation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=40, verbose_name='Compte de facturation')),
            ],
        ),
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.BooleanField(default=True, verbose_name='Actif')),
            ],
        ),
        migrations.CreateModel(
            name='Forfait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20, verbose_name='Forfait')),
                ('montant', models.IntegerField()),
                ('montantPlafondVoix', models.IntegerField()),
                ('montantPlafondData', models.IntegerField()),
                ('plafondInterne', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Operateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifiant', models.IntegerField()),
                ('libelle', models.CharField(max_length=20, verbose_name='Opérateur')),
            ],
        ),
        migrations.CreateModel(
            name='Type_sim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20, verbose_name='type SIM')),
            ],
        ),
        migrations.RenameField(
            model_name='division',
            old_name='division',
            new_name='libelle',
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50, verbose_name='Numéro ticket')),
                ('dateDemande', models.DateField(verbose_name='Date de demande')),
                ('dateApprobation', models.DateField(verbose_name="Date d'approbation")),
                ('compte_facturation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.compte_facturation')),
            ],
        ),
        migrations.CreateModel(
            name='Sim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Numéro')),
                ('adresseIP', models.IntegerField(verbose_name='Adresse IP')),
                ('acces', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.acces_sim')),
                ('etat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.etat')),
                ('forfait', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.forfait')),
                ('operateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.operateur')),
            ],
        ),
        migrations.AddField(
            model_name='forfait',
            name='typeSim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.type_sim'),
        ),
        migrations.CreateModel(
            name='Affectation_sim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAffectation', models.DateField(auto_now=True, verbose_name="Date d'affectaion")),
                ('dateActivation', models.DateField(auto_now=True, verbose_name="Date d'activation")),
                ('dateDesactivation', models.DateField(auto_now=True, verbose_name='Date désactivation')),
                ('dateModification', models.DateField(auto_now=True, verbose_name='Date de Modification')),
                ('collaborateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.collaborateur')),
                ('sim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.sim')),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sim.ticket')),
            ],
        ),
    ]
