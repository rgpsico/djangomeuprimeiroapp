# Generated by Django 3.2.5 on 2021-07-13 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_produtos_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='usuario',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='venda_id',
            field=models.IntegerField(null=True),
        ),
    ]
