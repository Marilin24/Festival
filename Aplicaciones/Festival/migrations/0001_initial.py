# Generated by Django 5.0.6 on 2025-01-14 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
                ('redes_sociales', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('descripcion', models.TextField()),
                ('id_organizador', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField()),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('id_boleto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festival.boleto')),
            ],
        ),
        migrations.AddField(
            model_name='boleto',
            name='id_festival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festival.festival'),
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('escenario', models.CharField(max_length=100)),
                ('duracion_min', models.IntegerField()),
                ('id_artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festival.artista')),
                ('id_festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Festival.festival')),
            ],
        ),
    ]
