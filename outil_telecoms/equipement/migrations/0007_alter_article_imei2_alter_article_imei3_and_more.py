# Generated by Django 4.2 on 2023-06-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipement", "0006_alter_sortie_numsortie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="imei2",
            field=models.IntegerField(blank=True, null=True, verbose_name="IMEI 2"),
        ),
        migrations.AlterField(
            model_name="article",
            name="imei3",
            field=models.IntegerField(blank=True, null=True, verbose_name="IMEI 3"),
        ),
        migrations.AlterField(
            model_name="article",
            name="imei4",
            field=models.IntegerField(blank=True, null=True, verbose_name="IMEI 4"),
        ),
    ]
