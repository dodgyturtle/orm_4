# Generated by Django 3.1.8 on 2021-04-19 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20210415_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', related_query_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционирует'),
        ),
    ]