# Generated by Django 2.2.7 on 2019-11-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('pontos_turisticos', '0003_turisticpoint_atraction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turisticpoint',
            old_name='atraction',
            new_name='atractions',
        ),
        migrations.AddField(
            model_name='turisticpoint',
            name='comments',
            field=models.ManyToManyField(to='comentarios.Comment'),
        ),
    ]
