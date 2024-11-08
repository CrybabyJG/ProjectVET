# Generated by Django 4.2 on 2024-11-06 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicamento', '0001_initial'),
        ('estado_compra', '0001_initial'),
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('ID_Compra', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_Compra', models.CharField(max_length=10, unique=True, verbose_name='Codigo de compra')),
                ('Descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('Fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('ID_EstadoCompra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estado_compra.estadodecompra', verbose_name='Estado de la compra')),
                ('ID_Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedor.proveedor', verbose_name='proveedor')),
            ],
            options={
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('ID_DetalleCompra', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('ID_Compra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles', to='compra.compra')),
                ('ID_Medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicamento.medicamento', verbose_name='Medicamento')),
            ],
            options={
                'verbose_name_plural': 'Detalles de Compras',
            },
        ),
    ]
