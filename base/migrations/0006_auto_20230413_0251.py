# Generated by Django 3.2.6 on 2023-04-12 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_comment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]