# Generated by Django 4.2 on 2023-06-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0025_remove_forfait_effectif'),
    ]

    operations = [
        migrations.AddField(
            model_name='sim',
            name='effectif',
            field=models.DateField(null=True),
        ),
    ]
