# Generated by Django 3.0.8 on 2020-09-17 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("chat_posts", "0018_handle_fk_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="handles",
            name="chat_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="chat_posts.ChatUsers",
            ),
        ),
    ]
