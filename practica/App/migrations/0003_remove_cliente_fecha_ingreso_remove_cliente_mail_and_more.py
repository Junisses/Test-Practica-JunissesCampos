# Generated by Django 4.1.7 on 2023-03-09 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_estado_etapa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='fecha_ingreso',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='sexo',
        ),
        migrations.CreateModel(
            name='Prospecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('mail', models.TextField(max_length=100)),
                ('telefono', models.TextField(max_length=9)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('sexo', models.TextField(max_length=12)),
                ('cliente_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.cliente')),
                ('estado_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.estado')),
                ('etapa_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.etapa')),
            ],
        ),
    ]
