# Generated by Django 3.1.2 on 2020-10-17 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('rut', models.CharField(max_length=12, verbose_name='Rut')),
                ('nombres', models.CharField(blank=True, max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=100, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(blank=True, max_length=100, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, max_length=100, verbose_name='Celular')),
                ('direccion1', models.CharField(blank=True, max_length=100, verbose_name='Dirección')),
                ('direccion2', models.CharField(blank=True, max_length=100, verbose_name='Dirección 2')),
                ('comuna', models.CharField(blank=True, max_length=100, verbose_name='Comuna')),
                ('region', models.CharField(blank=True, choices=[('1', 'I Región de Tarapacá'), ('2', 'II Región de Antofagasta'), ('3', 'III Región de Atacama'), ('4', 'IV Región de Coquimbo'), ('5', 'V Región de Valparaíso'), ('6', 'VI Región del Libertador General Bernardo O’Higgins'), ('7', 'VII Región del Maule'), ('8', 'VIII Región del Biobío'), ('9', 'IX Región de La Araucanía'), ('10', 'X Región de Los Lagos'), ('11', 'XI Región Aysén del General Carlos Ibáñez del Campo'), ('12', 'XII Región de Magallanes y Antártica Chilena'), ('13', 'Región Metropolitana de Santiago'), ('14', 'XIV Región de Los Ríos'), ('15', 'XV Región de Arica y Parinacota'), ('16', 'XVI Región de Ñuble')], max_length=100, verbose_name='Región')),
                ('pais', models.CharField(blank=True, max_length=100, verbose_name='País')),
                ('tipoFacturacion', models.CharField(blank=True, choices=[('1', 'Boleta'), ('2', 'Factura')], max_length=1, verbose_name='Tipo de facturación')),
                ('rutEmpresa', models.CharField(blank=True, max_length=100, verbose_name='Rut de la empresa')),
                ('nombreEmpresa', models.CharField(blank=True, max_length=100, verbose_name='Nombre de la empresa')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('exchange_id', models.CharField(blank=True, max_length=255, null=True)),
                ('event_start', models.DateTimeField(blank=True, null=True)),
                ('event_end', models.DateTimeField(blank=True, null=True)),
                ('event_subject', models.CharField(blank=True, max_length=255, null=True)),
                ('event_location', models.CharField(blank=True, max_length=255, null=True)),
                ('event_category', models.CharField(blank=True, max_length=255, null=True)),
                ('event_attendees', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('especie', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('sexo', models.CharField(blank=True, choices=[('1', 'Macho'), ('2', 'Hembra')], max_length=1, verbose_name='Sexo')),
                ('peso', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.clientes')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Veterinarias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('nombreVeterinario', models.CharField(blank=True, max_length=100, verbose_name='Nombre veterinario')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(blank=True, max_length=100, verbose_name='Teléfono')),
                ('celular', models.CharField(blank=True, max_length=100, verbose_name='Celular')),
                ('direccion1', models.CharField(blank=True, max_length=100, verbose_name='Dirección')),
                ('direccion2', models.CharField(blank=True, max_length=100, verbose_name='Dirección 2')),
                ('comuna', models.CharField(blank=True, max_length=100, verbose_name='Comuna')),
                ('region', models.CharField(blank=True, choices=[('1', 'I Región de Tarapacá'), ('2', 'II Región de Antofagasta'), ('3', 'III Región de Atacama'), ('4', 'IV Región de Coquimbo'), ('5', 'V Región de Valparaíso'), ('6', 'VI Región del Libertador General Bernardo O’Higgins'), ('7', 'VII Región del Maule'), ('8', 'VIII Región del Biobío'), ('9', 'IX Región de La Araucanía'), ('10', 'X Región de Los Lagos'), ('11', 'XI Región Aysén del General Carlos Ibáñez del Campo'), ('12', 'XII Región de Magallanes y Antártica Chilena'), ('13', 'Región Metropolitana de Santiago'), ('14', 'XIV Región de Los Ríos'), ('15', 'XV Región de Arica y Parinacota'), ('16', 'XVI Región de Ñuble')], max_length=100, verbose_name='Región')),
                ('pais', models.CharField(blank=True, max_length=100, verbose_name='País')),
            ],
            options={
                'verbose_name': 'Veterinaria',
                'verbose_name_plural': 'Veterinarias',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fechaCompra', models.DateField()),
                ('fechaVencimiento', models.DateField()),
                ('Descripción', models.CharField(max_length=200)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.proveedor')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Patologias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fechaCreacion', models.DateField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.pacientes')),
            ],
        ),
        migrations.AddField(
            model_name='pacientes',
            name='veterinarioAnterior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.veterinarias'),
        ),
        migrations.CreateModel(
            name='Muertes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('idConsulta', models.IntegerField()),
                ('razon', models.CharField(max_length=100)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.IntegerField()),
                ('idUsuario', models.IntegerField()),
                ('razon', models.CharField(max_length=100)),
                ('anamnesis', models.CharField(max_length=100)),
                ('examenFisico', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
                ('temperatura', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='Ciclos_Celo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='Alimentacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateField()),
                ('tipoComida', models.CharField(max_length=100)),
                ('marcaComida', models.CharField(max_length=100)),
                ('pesoComida', models.IntegerField()),
                ('nComidasDia', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.pacientes')),
            ],
        ),
    ]
