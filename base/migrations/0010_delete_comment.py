# Generated by Django 3.2.6 on 2023-04-12 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20230413_0425'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]