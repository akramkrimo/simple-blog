# Generated by Django 2.2.3 on 2019-10-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20191027_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='number_of_reads',
            field=models.IntegerField(default=0),
        ),
    ]
