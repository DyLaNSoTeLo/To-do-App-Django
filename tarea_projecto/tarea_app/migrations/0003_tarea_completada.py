# Generated by Django 4.2.7 on 2023-12-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea_app', '0002_mimodelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='completada',
            field=models.BooleanField(default=False),
        ),
    ]
