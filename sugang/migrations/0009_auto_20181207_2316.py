# Generated by Django 2.1.2 on 2018-12-07 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sugang', '0008_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='i_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sugang.Instructor'),
        ),
    ]
