# Generated by Django 3.0.5 on 2020-05-16 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicativoreceitas', '0004_receita_imagem_receita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='cozinheiro',
        ),
        migrations.AddField(
            model_name='receita',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
