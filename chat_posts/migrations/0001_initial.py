# Generated by Django 3.0.8 on 2020-07-31 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllowedIn",
            fields=[
                (
                    "username",
                    models.CharField(
                        db_column="userName",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
            ],
            options={
                "db_table": "AllowedIn",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Censors",
            fields=[
                (
                    "matchedtext",
                    models.CharField(
                        db_column="matchedText",
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
                (
                    "replacementtext",
                    models.CharField(db_column="replacementText", max_length=100),
                ),
            ],
            options={
                "db_table": "Censors",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ChatControls",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("ccurl", models.TextField(blank=True, db_column="ccURL", null=True)),
                ("height", models.CharField(max_length=5)),
            ],
            options={
                "db_table": "ChatControls",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CurrentPosts",
            fields=[
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
                ("handlename", models.CharField(db_column="handleName", max_length=50)),
                ("data", models.TextField(blank=True, null=True)),
                ("usertopm", models.CharField(db_column="userToPM", max_length=30)),
                (
                    "tstamp",
                    models.DateTimeField(
                        db_column="tStamp", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "CurrentPosts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DailyPosts",
            fields=[
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
                ("handlename", models.CharField(db_column="handleName", max_length=50)),
                ("data", models.TextField(blank=True, null=True)),
                ("usertopm", models.CharField(db_column="userToPM", max_length=30)),
                (
                    "tstamp",
                    models.DateTimeField(
                        db_column="tStamp", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "DailyPosts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Emoticons",
            fields=[
                (
                    "matchedtext",
                    models.CharField(
                        db_column="matchedText",
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "height",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=4, null=True
                    ),
                ),
                (
                    "width",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=4, null=True
                    ),
                ),
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
                (
                    "imageurl",
                    models.TextField(blank=True, db_column="imageURL", null=True),
                ),
            ],
            options={
                "db_table": "Emoticons",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="HandleOf",
            fields=[
                (
                    "handlename",
                    models.CharField(
                        db_column="handleName",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True, db_column="userName", max_length=30, null=True
                    ),
                ),
            ],
            options={
                "db_table": "HandleOf",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Handles",
            fields=[
                (
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "handlecolor",
                    models.CharField(
                        blank=True, db_column="handleColor", max_length=6, null=True
                    ),
                ),
                (
                    "textcolor",
                    models.CharField(
                        blank=True, db_column="textColor", max_length=6, null=True
                    ),
                ),
                (
                    "size",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=2, null=True
                    ),
                ),
                ("font", models.CharField(blank=True, max_length=50, null=True)),
                ("picture", models.TextField(blank=True, null=True)),
                ("link", models.TextField(blank=True, null=True)),
                ("hidden", models.IntegerField()),
            ],
            options={
                "db_table": "Handles",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="LegacyPosts",
            fields=[
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
                ("handlename", models.CharField(db_column="handleName", max_length=50)),
                ("data", models.TextField(blank=True, null=True)),
                ("usertopm", models.CharField(db_column="userToPM", max_length=30)),
                (
                    "tstamp",
                    models.DateTimeField(
                        db_column="tStamp", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "legacyposts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="OldSSUPosts",
            fields=[
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
                ("handlename", models.CharField(db_column="handleName", max_length=50)),
                ("data", models.TextField(blank=True, null=True)),
                ("usertopm", models.CharField(db_column="userToPM", max_length=30)),
                (
                    "tstamp",
                    models.DateTimeField(
                        db_column="tStamp", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "OldSSUPosts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Posts",
            fields=[
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
                ("handlename", models.CharField(db_column="handleName", max_length=50)),
                ("data", models.TextField(blank=True, null=True)),
                ("usertopm", models.CharField(db_column="userToPM", max_length=30)),
                (
                    "tstamp",
                    models.DateTimeField(
                        db_column="tStamp", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "Posts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Profiles",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(db_column="UserName", max_length=12)),
            ],
            options={
                "db_table": "Profiles",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RoomAdmins",
            fields=[
                (
                    "username",
                    models.CharField(
                        db_column="userName",
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
            ],
            options={
                "db_table": "RoomAdmins",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Rooms",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("motd", models.TextField(blank=True, null=True)),
                ("timecreated", models.DateTimeField(db_column="timeCreated")),
            ],
            options={
                "db_table": "Rooms",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Skins",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                (
                    "styleurl",
                    models.TextField(blank=True, db_column="styleURL", null=True),
                ),
            ],
            options={
                "db_table": "Skins",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TrumpPost",
            fields=[
                ("roomname", models.CharField(db_column="roomName", max_length=30)),
                ("handlename", models.CharField(db_column="handleName", max_length=50)),
                ("data", models.TextField(blank=True, null=True)),
                ("usertopm", models.CharField(db_column="userToPM", max_length=30)),
                (
                    "tstamp",
                    models.DateTimeField(
                        db_column="tStamp", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "trumpPost",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(blank=True, max_length=32, null=True)),
                (
                    "preferredname",
                    models.CharField(
                        blank=True, db_column="preferredName", max_length=30, null=True
                    ),
                ),
                (
                    "realname",
                    models.CharField(
                        blank=True, db_column="realName", max_length=40, null=True
                    ),
                ),
                ("birthday", models.DateField(blank=True, null=True)),
                (
                    "emailaddress",
                    models.CharField(db_column="emailAddress", max_length=100),
                ),
                ("timemodified", models.DateTimeField(db_column="timeModified")),
                (
                    "defaulthandle",
                    models.CharField(
                        blank=True, db_column="defaultHandle", max_length=50, null=True
                    ),
                ),
                (
                    "defaultroom",
                    models.CharField(
                        blank=True, db_column="defaultRoom", max_length=30, null=True
                    ),
                ),
                (
                    "avatarlayout",
                    models.CharField(db_column="avatarLayout", max_length=10),
                ),
                ("avatartime", models.CharField(db_column="avatarTime", max_length=4)),
                ("avatarpictures", models.IntegerField(db_column="avatarPictures")),
                ("systemmessages", models.IntegerField(db_column="systemMessages")),
                ("emoticons", models.IntegerField()),
                ("skin", models.CharField(max_length=30)),
                ("chatcontrol", models.CharField(max_length=30)),
                ("refresh", models.DecimalField(decimal_places=0, max_digits=10)),
                ("avatarlimit", models.DecimalField(decimal_places=0, max_digits=10)),
                ("chatlimit", models.DecimalField(decimal_places=0, max_digits=10)),
                ("framestyle", models.CharField(max_length=20)),
                ("javascript", models.IntegerField()),
                ("frameborder", models.IntegerField()),
                ("scrollbar", models.IntegerField()),
                ("timecreated", models.DateTimeField(db_column="timeCreated")),
                ("autoloadrecent", models.IntegerField(db_column="autoloadRecent")),
                (
                    "timezoneoffset",
                    models.DecimalField(
                        db_column="timezoneOffset", decimal_places=0, max_digits=2
                    ),
                ),
                (
                    "allowskinoverride",
                    models.IntegerField(db_column="allowSkinOverride"),
                ),
                ("scratchpadtext", models.TextField(db_column="scratchpadText")),
                (
                    "scratchpadtime",
                    models.DateTimeField(
                        blank=True, db_column="scratchpadTime", null=True
                    ),
                ),
                ("location", models.TextField()),
                ("aim", models.TextField(db_column="AIM")),
                ("icq", models.TextField(db_column="ICQ")),
                ("msn", models.TextField(db_column="MSN")),
                ("firstcame", models.TextField(db_column="firstCame")),
                ("interests", models.TextField()),
                ("obsessions", models.TextField()),
                (
                    "favoritevideogames",
                    models.TextField(db_column="favoriteVideoGames"),
                ),
                ("favoriteanime", models.TextField(db_column="favoriteAnime")),
                ("favoritemusic", models.TextField(db_column="favoriteMusic")),
                ("mosttimespent", models.TextField(db_column="mostTimeSpent")),
                ("futureaspirations", models.TextField(db_column="futureAspirations")),
                ("randomphrase", models.TextField(db_column="randomPhrase")),
                ("personalquote", models.TextField(db_column="personalQuote")),
            ],
            options={
                "db_table": "Users",
            },
        ),
    ]
