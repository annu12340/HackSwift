# Generated by Django 3.2.8 on 2022-06-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0015_auto_20220623_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='qrcode_id',
            field=models.IntegerField(default=0),
        ),
    ]
