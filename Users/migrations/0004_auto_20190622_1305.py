# Generated by Django 2.1.7 on 2019-06-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20190619_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_column='UserName', max_length=255, unique=True),
        ),
    ]
