# Generated by Django 4.0.4 on 2022-11-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_device_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cracked_tools',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='firmwares',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='frp_bypass',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='videotorent',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
