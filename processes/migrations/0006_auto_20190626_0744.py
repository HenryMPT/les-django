# Generated by Django 2.1.7 on 2019-06-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0005_auto_20190626_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
    ]