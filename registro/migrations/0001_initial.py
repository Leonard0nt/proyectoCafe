# Generated by Django 5.0.6 on 2024-06-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('Reclamo', 'Reclamo'), ('Felicitaciones', 'Felicitaciones')], max_length=20)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]