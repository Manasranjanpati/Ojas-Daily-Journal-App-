# Generated by Django 3.2 on 2021-04-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
