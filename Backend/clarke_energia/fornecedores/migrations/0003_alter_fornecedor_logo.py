# Generated by Django 5.0.1 on 2024-01-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0002_alter_fornecedor_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='fornecedores/logos/'),
        ),
    ]
