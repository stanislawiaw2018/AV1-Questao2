# Generated by Django 2.2.6 on 2019-10-26 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datai', models.DateField(verbose_name='Data Inicio')),
                ('dataf', models.DateField(verbose_name='Data Termino')),
                ('horai', models.TimeField(verbose_name='Horario Inicial')),
                ('horaf', models.TimeField(verbose_name='Horario Termino')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('carga', models.IntegerField(verbose_name='Carga Horaria')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Hora/aula')),
                ('Turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Turma')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga_Horaria')),
                ('ementa', models.TextField(verbose_name='Ementa')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor_curso')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Turma')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
    ]
