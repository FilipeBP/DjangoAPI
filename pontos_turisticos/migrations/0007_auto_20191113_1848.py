# Generated by Django 2.2.7 on 2019-11-13 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0006_turisticpoint_localization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turisticpoint',
            name='localization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacao.Localization'),
        ),
    ]
