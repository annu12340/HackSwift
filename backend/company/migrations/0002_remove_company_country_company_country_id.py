# Generated by Django 4.2.5 on 2023-09-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.AddField(
            model_name='company',
            name='country_id',
            field=models.IntegerField(default=0),
        ),
    ]
