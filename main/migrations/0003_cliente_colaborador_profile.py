# Generated by Django 3.1 on 2020-09-26 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_identidad', models.CharField(max_length=8)),
                ('fecha_nacimiento', models.DateField()),
                ('estado', models.CharField(max_length=3)),
                ('genero', models.CharField(choices=[('MA', 'Masculino'), ('FE', 'Femenino'), ('NB', 'No Binario')], max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reputacion', models.FloatField()),
                ('cobertura_entrega', models.ManyToManyField(to='main.Localizacion')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferencias', models.ManyToManyField(to='main.Categoria')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]
