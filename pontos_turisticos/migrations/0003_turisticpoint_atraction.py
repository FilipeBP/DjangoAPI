# Generated by Django 2.2.7 on 2019-11-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('pontos_turisticos', '0002_auto_20191113_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='turisticpoint',
            name='atraction',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
