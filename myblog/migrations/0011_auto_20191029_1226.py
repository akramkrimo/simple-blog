# Generated by Django 2.2.3 on 2019-10-29 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20191029_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='paren_comment',
            new_name='parent_comment',
        ),
    ]