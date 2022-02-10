# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Emoticons(models.Model):
    matchedtext = models.CharField(
        db_column="matchedText", primary_key=True, max_length=100
    )  # Field name made lowercase.
    height = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    width = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    roomname = models.CharField(
        db_column="roomName", max_length=30
    )  # Field name made lowercase.
    imageurl = models.TextField(
        db_column="imageURL", blank=True, null=True
    )  # Field name made lowercase.


class ChatUsers(models.Model):
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    preferred_name = models.CharField(
        db_column="preferred_name", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    real_name = models.CharField(
        db_column="real_name", max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    birthday = models.DateField(blank=True, null=True)
    email_address = models.CharField(
        db_column="email_address", max_length=100
    )  # Field name made lowercase.
    time_modified = models.DateTimeField(
        db_column="time_modified"
    )  # Field name made lowercase.
    default_handle = models.CharField(
        db_column="default_handle", max_length=50, blank=True, null=True
    )  # Field name made lowercase.
    default_room = models.CharField(
        db_column="default_room", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    avatar_layout = models.CharField(
        db_column="avatar_layout", max_length=10
    )  # Field name made lowercase.
    avatar_time = models.CharField(
        db_column="avatar_time", max_length=4
    )  # Field name made lowercase.
    avatar_pictures = models.IntegerField(
        db_column="avatar_pictures"
    )  # Field name made lowercase.
    system_messages = models.IntegerField(
        db_column="system_messages"
    )  # Field name made lowercase.
    time_created = models.DateTimeField(
        db_column="time_created"
    )  # Field name made lowercase.
    autoload_recent = models.IntegerField(
        db_column="autoload_recent"
    )  # Field name made lowercase.
    timezone_offset = models.DecimalField(
        db_column="timezone_offset", max_digits=2, decimal_places=0
    )  # Field name made lowercase.
    allow_skin_override = models.IntegerField(
        db_column="allow_skin_override"
    )  # Field name made lowercase.
    scratchpad_text = models.TextField(
        db_column="scratchpad_text"
    )  # Field name made lowercase.
    scratchpad_time = models.DateTimeField(
        db_column="scratchpad_time", blank=True, null=True
    )  # Field name made lowercase.
    location = models.TextField()
    aim = models.TextField(db_column="AIM")  # Field name made lowercase.
    icq = models.TextField(db_column="ICQ")  # Field name made lowercase.
    msn = models.TextField(db_column="MSN")  # Field name made lowercase.
    first_came = models.TextField(db_column="first_came")  # Field name made lowercase.
    interests = models.TextField()
    obsessions = models.TextField()
    favorite_video_games = models.TextField(
        db_column="favorite_video_games"
    )  # Field name made lowercase.
    favorite_anime = models.TextField(
        db_column="favorite_anime"
    )  # Field name made lowercase.
    favorite_music = models.TextField(
        db_column="favorite_music"
    )  # Field name made lowercase.
    most_time_spent = models.TextField(
        db_column="most_time_spent"
    )  # Field name made lowercase.
    future_aspirations = models.TextField(
        db_column="future_aspirations"
    )  # Field name made lowercase.
    random_phrase = models.TextField(
        db_column="random_phrase"
    )  # Field name made lowercase.
    personal_quote = models.TextField(
        db_column="personal_quote"
    )  # Field name made lowercase.


class Handles(models.Model):
    name = models.CharField(unique=True, max_length=50)
    handle_color = models.CharField(
        db_column="handle_color", max_length=6, blank=True, null=True
    )  # Field name made lowercase.
    text_color = models.CharField(
        db_column="text_color", max_length=6, blank=True, null=True
    )  # Field name made lowercase.
    size = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    font = models.CharField(max_length=50, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()

    chat_user = models.ForeignKey(
        ChatUsers, null=True, blank=True, on_delete=models.SET_NULL
    )


class Rooms(models.Model):
    name = models.CharField(max_length=30)
    motd = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(
        db_column="time_created"
    )  # Field name made lowercase.


class Posts(models.Model):
    message = models.TextField(blank=True, null=True)
    user_to_pm = models.CharField(
        db_column="user_to_PM", max_length=30
    )  # Field name made lowercase.
    datetime_posted = models.DateTimeField(
        db_column="datetime_posted"
    )  # Field name made lowercase.

    room = models.ForeignKey(Rooms, null=True, blank=True, on_delete=models.SET_NULL)
    handle = models.ForeignKey(
        Handles, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ["datetime_posted"]
