# Generated by Django 2.1.7 on 2019-06-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0009_auto_20190625_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='verb_sug',
            field=models.CharField(blank=True, db_column='VerbSug', max_length=255, verbose_name='Verbo Sugerido'),
        ),
    ]
