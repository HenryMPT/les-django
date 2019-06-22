# Generated by Django 2.1.7 on 2019-06-22 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artefact',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('artefactname', models.CharField(db_column='ArtefactName', max_length=255, unique=True, verbose_name='Artefacto')),
                ('datecreated', models.DateField(db_column='DateCreated')),
            ],
            options={
                'db_table': 'Artefacto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('groupname', models.CharField(blank=True, db_column='GroupName', max_length=255, null=True, unique=True)),
                ('creationdate', models.DateField(blank=True, db_column='CreationDate', null=True)),
                ('name', models.CharField(db_column='Name', max_length=255)),
                ('description', models.CharField(db_column='Description', max_length=255)),
            ],
            options={
                'db_table': 'Group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('patternname', models.CharField(db_column='PatternName', max_length=255)),
                ('image', models.TextField(blank=True, db_column='Image', null=True)),
                ('description', models.CharField(db_column='Description', max_length=255)),
                ('data_creation', models.DateField(db_column='Data Creation', null=True)),
                ('groups', models.ManyToManyField(to='Activities.Group')),
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Pattern',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('resourcename', models.CharField(db_column='ResourceName', max_length=255, unique=True, verbose_name='Recurso')),
                ('datecreated', models.DateField(db_column='DateCreated')),
            ],
            options={
                'db_table': 'Resource',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sentencename', models.CharField(db_column='SentenceName', max_length=255, verbose_name='Frase')),
                ('datecreated', models.DateField(db_column='DateCreated', null=True)),
                ('subject', models.CharField(db_column='Subject', max_length=255, verbose_name='Sujeito')),
                ('receiver', models.CharField(blank=True, db_column='Receiver', max_length=255, null=True, verbose_name='Recetor')),
                ('datarealizado', models.DateField(blank=True, db_column='DataRealizado', null=True)),
                ('recurso', models.CharField(blank=True, db_column='Recurso', max_length=255, null=True)),
                ('artefacto', models.CharField(blank=True, db_column='Artefacto', max_length=255, null=True)),
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Sentence',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('name', models.IntegerField(blank=True, db_column='Name', null=True)),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Tags',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('verbname', models.CharField(db_column='VerbName', max_length=255, unique=True, verbose_name='Verbo')),
                ('verbtype', models.CharField(choices=[('Produtivo', 'Produtivo'), ('Comunicativo', 'Comunicativo')], db_column='VerbType', max_length=255, verbose_name='Tipo')),
            ],
            options={
                'db_table': 'Verb',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='sentence',
            name='verbid',
            field=models.ForeignKey(db_column='VerbID', on_delete=django.db.models.deletion.DO_NOTHING, to='Activities.Verb', verbose_name='Verbo'),
        ),
        migrations.AddField(
            model_name='group',
            name='sentences',
            field=models.ManyToManyField(to='Activities.Sentence'),
        ),
        migrations.AddField(
            model_name='group',
            name='tags',
            field=models.ManyToManyField(to='Activities.Tags'),
        ),
        migrations.AddField(
            model_name='group',
            name='userid',
            field=models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
