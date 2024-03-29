# Generated by Django 5.0.2 on 2024-02-21 15:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_board_board_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='started',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='board',
            name='board_type',
            field=models.CharField(choices=[('Todo', 'todo'), ('Doing', 'doing'), ('Done', 'Done')], default='Doing', max_length=8),
        ),
    ]
