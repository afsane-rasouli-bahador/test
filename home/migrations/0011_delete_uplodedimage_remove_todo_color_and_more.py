# Generated by Django 5.0.2 on 2024-02-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_todo_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UplodedImage',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='color',
        ),
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]