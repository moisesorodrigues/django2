# Generated by Django 3.0.5 on 2020-05-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativoreceitas', '0002_receita_cozinheiro'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='modo_edicao',
            field=models.BooleanField(default=False),
        ),
    ]