# Generated by Django 3.2.5 on 2021-07-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210711_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='item',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='quantidade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='usuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='valor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
