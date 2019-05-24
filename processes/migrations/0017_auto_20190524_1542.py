# Generated by Django 2.1.7 on 2019-05-24 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0016_auto_20190523_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='pattern',
            field=models.ManyToManyField(blank=True, to='Activities.Pattern'),
        ),
        migrations.AlterField(
            model_name='process',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 14, 42, 9, 251093, tzinfo=utc), verbose_name='date created'),
        ),
    ]
