# Generated by Django 5.0.1 on 2024-02-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_protagonista_personaje_pelicula_personaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='resumen',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
