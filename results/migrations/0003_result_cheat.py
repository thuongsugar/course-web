# Generated by Django 3.2.9 on 2022-01-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_result_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='cheat',
            field=models.IntegerField(default=0),
        ),
    ]
