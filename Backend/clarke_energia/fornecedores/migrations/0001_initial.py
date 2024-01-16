# Generated by Django 5.0.1 on 2024-01-15 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='fornecedores/logos/')),
                ('estado', models.CharField(max_length=50)),
                ('custo_por_kwh', models.DecimalField(decimal_places=2, max_digits=5)),
                ('limite_minimo_kwh', models.PositiveIntegerField()),
                ('num_total_clientes', models.PositiveIntegerField()),
                ('avaliacao_media', models.FloatField()),
            ],
        ),
    ]