# Generated by Django 4.2 on 2024-10-27 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('ID_Presentacion', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_Presentacion', models.CharField(max_length=10, unique=True, verbose_name='Codigo de presentacion')),
                ('Peso', models.CharField(max_length=40, verbose_name='Peso')),
            ],
            options={
                'verbose_name': 'Presentacione',
            },
        ),
    ]