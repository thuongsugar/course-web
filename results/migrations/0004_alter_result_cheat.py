# Generated by Django 3.2.9 on 2022-01-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_result_cheat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='cheat',
            field=models.IntegerField(),
        ),
    ]
