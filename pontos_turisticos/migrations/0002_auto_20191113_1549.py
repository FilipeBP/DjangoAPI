# Generated by Django 2.2.7 on 2019-11-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turisticpoint',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
