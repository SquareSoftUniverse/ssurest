# Generated by Django 3.0.8 on 2020-07-31 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat_posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="id",
            field=models.IntegerField(default=0),
        ),
    ]
