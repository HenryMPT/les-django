# Generated by Django 2.1.7 on 2019-05-24 14:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0018_auto_20190524_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='pattern',
            field=models.ManyToManyField(blank=True, null=True, to='Activities.Pattern'),
        ),
        migrations.AlterField(
            model_name='process',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 14, 52, 47, 803331, tzinfo=utc), verbose_name='date created'),
        ),
    ]
