# Generated by Django 2.1.7 on 2019-06-25 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0005_auto_20190624_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='description',
            field=models.TextField(db_column='Description'),
        ),
    ]
