# Generated by Django 2.1.2 on 2018-11-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_categorize', models.CharField(max_length=10)),
                ('sub_name', models.CharField(max_length=30)),
                ('sub_code', models.CharField(max_length=10)),
                ('i_name', models.CharField(max_length=10)),
                ('i_code', models.CharField(max_length=10)),
                ('total_lecture', models.IntegerField(default=0)),
                ('lecture_level', models.CharField(max_length=10)),
                ('book', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Take',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=20)),
                ('take_start', models.DateTimeField(verbose_name='date started')),
                ('take_end', models.DateTimeField(verbose_name='date ended')),
            ],
        ),
    ]
