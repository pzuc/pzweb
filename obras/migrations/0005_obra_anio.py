# Generated by Django 4.0.2 on 2022-06-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0004_obra_bajada_obra_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='anio',
            field=models.PositiveIntegerField(default=2014),
        ),
    ]
