# Generated by Django 5.0.2 on 2024-02-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
