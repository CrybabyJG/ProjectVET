# Generated by Django 4.2 on 2024-10-27 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estado_de_cita', '0001_initial'),
        ('enfermedades', '0001_initial'),
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('ID_Cita', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_Cita', models.CharField(max_length=10, unique=True, verbose_name='Codigo Cita')),
                ('Fecha_Realizacion', models.DateField(auto_now_add=True, verbose_name='Fecha de realizacion')),
                ('Fecha_de_Cita', models.DateField(auto_now_add=True, verbose_name='Fecha para cita')),
                ('Peso', models.CharField(max_length=30, verbose_name='Peso')),
                ('ID_EstadoCita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estado_de_cita.estadodecita', verbose_name='Estado de la cita')),
                ('ID_Mascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mascota.mascota', verbose_name='Mascota')),
            ],
            options={
                'verbose_name_plural': 'Citas',
            },
        ),
        migrations.CreateModel(
            name='Detalle_Cita',
            fields=[
                ('ID_DetalleCita', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_DetalleCita', models.CharField(max_length=10, unique=True, verbose_name='Codigo de detalle cita')),
                ('Descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('ID_Cita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cita.cita', verbose_name='Cita No')),
                ('ID_Enfermedades', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Detalles', to='enfermedades.enfermedades')),
            ],
            options={
                'verbose_name_plural': 'Detalles de Citas',
            },
        ),
    ]
