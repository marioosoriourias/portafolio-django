# Generated by Django 4.0.3 on 2022-03-18 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='habilidades')),
            ],
        ),
        migrations.CreateModel(
            name='SobreMi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripcion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='proyectos')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.skills')),
            ],
        ),
    ]
