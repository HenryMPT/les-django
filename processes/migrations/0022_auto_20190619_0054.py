# Generated by Django 2.1.7 on 2019-06-18 23:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0021_auto_20190618_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]
