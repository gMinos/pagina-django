# Generated by Django 5.0.6 on 2024-05-13 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_remove_preferencia_plato_delete_plato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.BinaryField()),
            ],
        ),
        migrations.AddField(
            model_name='preferencia',
            name='comida',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='miapp.comida'),
        ),
    ]