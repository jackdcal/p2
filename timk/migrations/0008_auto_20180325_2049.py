# Generated by Django 2.0.3 on 2018-03-25 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timk', '0007_auto_20180325_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='teams',
        ),
        migrations.AddField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(limit_choices_to={'group': models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')], default='A', max_length=1)}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team1', to='timk.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(limit_choices_to={'group': models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H')], default='A', max_length=1)}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team2', to='timk.Team'),
        ),
    ]