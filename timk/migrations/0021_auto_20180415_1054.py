# Generated by Django 2.0.3 on 2018-04-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timk', '0020_auto_20180415_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='duration',
            field=models.TimeField(default=''),
        ),
    ]