# Generated by Django 2.1.7 on 2019-03-27 11:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190326_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_role',
            new_name='user_profile',
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 11, 33, 9, 627071, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='process',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 11, 33, 9, 627071, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 11, 33, 9, 629023, tzinfo=utc), verbose_name='date published'),
        ),
    ]
