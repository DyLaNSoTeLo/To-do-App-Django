# Generated by Django 4.2.7 on 2023-12-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mimodelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(max_length=50)),
                ('campo2', models.IntegerField()),
            ],
        ),
    ]
