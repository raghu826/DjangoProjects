# Generated by Django 3.1.4 on 2021-01-09 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/static'),
        ),
    ]
