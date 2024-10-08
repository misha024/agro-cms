# Generated by Django 5.0.7 on 2024-08-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_slidercardsdescriptions_alter_slidercards_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slidercardsdescriptions',
            options={'verbose_name': 'Преимущество', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AddField(
            model_name='slidercards',
            name='href',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='slidercards',
            name='descriptions',
            field=models.ManyToManyField(blank=True, to='main.slidercardsdescriptions', verbose_name='Преимущества'),
        ),
    ]
