# Generated by Django 4.1.7 on 2023-07-16 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0019_alter_campaign_asset_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='asset_id',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='qrcode_url',
        ),
    ]