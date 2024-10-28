# Generated by Django 4.2 on 2024-10-27 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('medicamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('ID_Venta', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_Venta', models.CharField(max_length=10, unique=True, verbose_name='Codigo de venta')),
                ('Descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('Fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('ID_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.clientes', verbose_name='Nombre del cliente')),
            ],
            options={
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('ID_DetalleVenta', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('ID_Medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicamento.medicamento', verbose_name='Medicamento')),
                ('ID_Venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Detalles', to='venta.venta')),
            ],
            options={
                'verbose_name_plural': 'Detalles de ventas',
            },
        ),
    ]
