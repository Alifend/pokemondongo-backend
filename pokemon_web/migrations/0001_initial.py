# Generated by Django 3.2 on 2021-11-28 15:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berries',
            fields=[
                ('Descripcion', models.CharField(max_length=400)),
                ('Nombre', models.CharField(max_length=20)),
                ('Identificador', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField(default=1)),
                ('imagen_berrie', models.URLField(max_length=900)),
                ('Costo', models.IntegerField(default=1)),
                ('Efectoestadistico', models.IntegerField(default=0)),
                ('EfectoEstado', models.CharField(choices=[('Normal', 'Normal'), ('Sin Efecto', 'Sin Efecto')], default='Sin Efecto', max_length=20)),
            ],
            options={
                'ordering': ['Nombre'],
            },
        ),
        migrations.CreateModel(
            name='EntrenadorPK',
            fields=[
                ('Fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha (Año/Mes/Dia)')),
                ('ID', models.CharField(default='0', max_length=40, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=20)),
                ('Password2', models.CharField(max_length=20)),
                ('Imagen_Perfil', models.URLField(max_length=900)),
                ('Dinero', models.IntegerField()),
            ],
            options={
                'ordering': ['Fecha'],
            },
        ),
        migrations.CreateModel(
            name='Maquina_EntrenadorPK',
            fields=[
                ('ID', models.CharField(default='0', max_length=40, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Imagen_Perfil', models.URLField(max_length=900)),
                ('Dinero', models.IntegerField()),
                ('Dificultad', models.CharField(choices=[('Facil', 'Facil'), ('Medio', 'Medio'), ('Dificil', 'Dificil')], default='Facil', max_length=15)),
            ],
            options={
                'ordering': ['ID'],
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('ID', models.CharField(max_length=2000, primary_key=True, serialize=False)),
                ('Nombre_Pokemon', models.CharField(max_length=20)),
                ('Imagen_Pokemon', models.URLField(max_length=900)),
                ('XP', models.IntegerField(default=1)),
                ('HP', models.IntegerField(default=1)),
                ('Defensa', models.IntegerField(default=1)),
                ('Peso', models.IntegerField(default=1)),
                ('Altura', models.IntegerField(default=1)),
                ('Estado', models.CharField(choices=[('Confuso', 'Confuso'), ('Dormido', 'Dormido'), ('Quemado', 'Quemado'), ('Congelado', 'Congelado'), ('Paralizado', 'Paralizado'), ('Normal', 'Normal')], default='Normal', max_length=20)),
                ('Nivel', models.IntegerField(default=1)),
                ('ID_Entrenador', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='pokemon_web.entrenadorpk')),
                ('ID_Maquina', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='pokemon_web.maquina_entrenadorpk')),
            ],
            options={
                'ordering': ['ID'],
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('Nombre', models.CharField(max_length=20)),
                ('Daño', models.IntegerField(default=1)),
                ('Drenado', models.IntegerField(default=0)),
                ('Cantidad', models.IntegerField(default=1)),
                ('Efecto', models.CharField(choices=[('Confuso', 'Confuso'), ('Dormido', 'Dormido'), ('Quemado', 'Quemado'), ('Congelado', 'Congelado'), ('Paralizado', 'Paralizado'), ('Normal', 'Normal'), ('Sin Efecto', 'Sin Efecto')], default='Sin Efecto', max_length=20)),
                ('Identificador_MO', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('aumentos', models.IntegerField(default=0)),
                ('Id_Pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_web.pokemon')),
            ],
            options={
                'ordering': ['Nombre'],
            },
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('Descripcion', models.CharField(max_length=400)),
                ('Nombre', models.CharField(max_length=20)),
                ('Identificador', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Id_Pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_web.pokemon')),
            ],
            options={
                'ordering': ['Nombre'],
            },
        ),
    ]
