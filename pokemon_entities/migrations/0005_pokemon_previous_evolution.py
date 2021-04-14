# Generated by Django 3.1.8 on 2021-04-14 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20210414_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.pokemon'),
        ),
    ]
