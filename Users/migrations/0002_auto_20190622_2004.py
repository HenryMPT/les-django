# Generated by Django 2.1.7 on 2019-06-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='useremail',
            field=models.CharField(db_column='UserEmail', default='mailmail@mail.com', max_length=255),
            preserve_default=False,
        ),
    ]