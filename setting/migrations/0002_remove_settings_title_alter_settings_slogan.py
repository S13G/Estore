# Generated by Django 4.1.2 on 2022-10-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='title',
        ),
        migrations.AlterField(
            model_name='settings',
            name='slogan',
            field=models.TextField(),
        ),
    ]