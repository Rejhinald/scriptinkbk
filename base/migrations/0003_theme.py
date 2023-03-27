# Generated by Django 4.1.2 on 2023-03-27 05:18

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_delete_genre2_delete_genre3"),
    ]

    operations = [
        migrations.CreateModel(
            name="Theme",
            fields=[
                ("_id", models.AutoField(primary_key=True, serialize=False)),
                ("theme_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=base.models.upload_image_path
                    ),
                ),
                ("theme_description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
