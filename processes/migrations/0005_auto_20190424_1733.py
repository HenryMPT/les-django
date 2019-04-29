# Generated by Django 2.1.7 on 2019-04-24 16:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0004_auto_20190424_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 16, 33, 20, 591799, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='activity',
            field=models.ManyToManyField(blank=True, to='processes.Activity'),
        ),
    ]
