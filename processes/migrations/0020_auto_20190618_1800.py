# Generated by Django 2.1.7 on 2019-06-18 17:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0019_auto_20190524_1552'),
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
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 18, 17, 0, 55, 50886, tzinfo=utc), verbose_name='date created'),
        ),
    ]
