# Generated by Django 2.0.1 on 2018-01-21 02:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('infed', '0003_auto_20180121_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='certificate_expiry',
            new_name='not_valid_after',
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='not_valid_before',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
