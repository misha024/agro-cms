# Generated by Django 5.0.7 on 2024-08-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_mainsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainsettings',
            name='site_domain',
            field=models.CharField(default='localhost', max_length=250, verbose_name='Доменное имя сайта'),
        ),
    ]
