# Generated by Django 5.1.1 on 2024-09-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_alter_venda_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='endereco_entrega',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='venda',
            name='nome',
            field=models.TextField(max_length=50),
        ),
    ]
