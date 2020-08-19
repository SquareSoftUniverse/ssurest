# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllowedIn(models.Model):
    username = models.CharField(db_column='userName', primary_key=True, max_length=50)  # Field name made lowercase.
    roomname = models.CharField(db_column='roomName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllowedIn'


class Emoticons(models.Model):
    matchedtext = models.CharField(db_column='matchedText', primary_key=True, max_length=100)  # Field name made lowercase.
    height = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    width = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    roomname = models.CharField(db_column='roomName', max_length=30)  # Field name made lowercase.
    imageurl = models.TextField(db_column='imageURL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Emoticons'


class HandleOf(models.Model):
    handlename = models.CharField(db_column='handleName', primary_key=True, max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HandleOf'


class Handles(models.Model):
    name = models.CharField(unique=True, max_length=50)
    handlecolor = models.CharField(db_column='handleColor', max_length=6, blank=True, null=True)  # Field name made lowercase.
    textcolor = models.CharField(db_column='textColor', max_length=6, blank=True, null=True)  # Field name made lowercase.
    size = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    font = models.CharField(max_length=50, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()

    class Meta:
        db_table = 'Handles'


class Posts(models.Model):
    roomname = models.CharField(db_column='roomName', max_length=30)  # Field name made lowercase.
    handlename = models.CharField(db_column='handleName', max_length=50)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)
    usertopm = models.CharField(db_column='userToPM', max_length=30)  # Field name made lowercase.
    tstamp = models.DateTimeField(db_column='tStamp')  # Field name made lowercase.

    class Meta:
        db_table = 'Posts'


class RoomAdmins(models.Model):
    username = models.CharField(db_column='userName', primary_key=True, max_length=50)  # Field name made lowercase.
    roomname = models.CharField(db_column='roomName', max_length=30)  # Field name made lowercase.

    class Meta:
        db_table = 'RoomAdmins'


class Rooms(models.Model):
    name = models.CharField(max_length=30)
    motd = models.TextField(blank=True, null=True)
    timecreated = models.DateTimeField(db_column='timeCreated')  # Field name made lowercase.

    class Meta:
        db_table = 'Rooms'


class ChatUsers(models.Model):
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    preferredname = models.CharField(db_column='preferredName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='realName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField(blank=True, null=True)
    emailaddress = models.CharField(db_column='emailAddress', max_length=100)  # Field name made lowercase.
    timemodified = models.DateTimeField(db_column='timeModified')  # Field name made lowercase.
    defaulthandle = models.CharField(db_column='defaultHandle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    defaultroom = models.CharField(db_column='defaultRoom', max_length=30, blank=True, null=True)  # Field name made lowercase.
    avatarlayout = models.CharField(db_column='avatarLayout', max_length=10)  # Field name made lowercase.
    avatartime = models.CharField(db_column='avatarTime', max_length=4)  # Field name made lowercase.
    avatarpictures = models.IntegerField(db_column='avatarPictures')  # Field name made lowercase.
    systemmessages = models.IntegerField(db_column='systemMessages')  # Field name made lowercase.
    emoticons = models.IntegerField()
    skin = models.CharField(max_length=30)
    chatcontrol = models.CharField(max_length=30)
    refresh = models.DecimalField(max_digits=10, decimal_places=0)
    avatarlimit = models.DecimalField(max_digits=10, decimal_places=0)
    chatlimit = models.DecimalField(max_digits=10, decimal_places=0)
    framestyle = models.CharField(max_length=20)
    javascript = models.IntegerField()
    frameborder = models.IntegerField()
    scrollbar = models.IntegerField()
    timecreated = models.DateTimeField(db_column='timeCreated')  # Field name made lowercase.
    autoloadrecent = models.IntegerField(db_column='autoloadRecent')  # Field name made lowercase.
    timezoneoffset = models.DecimalField(db_column='timezoneOffset', max_digits=2, decimal_places=0)  # Field name made lowercase.
    allowskinoverride = models.IntegerField(db_column='allowSkinOverride')  # Field name made lowercase.
    scratchpadtext = models.TextField(db_column='scratchpadText')  # Field name made lowercase.
    scratchpadtime = models.DateTimeField(db_column='scratchpadTime', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField()
    aim = models.TextField(db_column='AIM')  # Field name made lowercase.
    icq = models.TextField(db_column='ICQ')  # Field name made lowercase.
    msn = models.TextField(db_column='MSN')  # Field name made lowercase.
    firstcame = models.TextField(db_column='firstCame')  # Field name made lowercase.
    interests = models.TextField()
    obsessions = models.TextField()
    favoritevideogames = models.TextField(db_column='favoriteVideoGames')  # Field name made lowercase.
    favoriteanime = models.TextField(db_column='favoriteAnime')  # Field name made lowercase.
    favoritemusic = models.TextField(db_column='favoriteMusic')  # Field name made lowercase.
    mosttimespent = models.TextField(db_column='mostTimeSpent')  # Field name made lowercase.
    futureaspirations = models.TextField(db_column='futureAspirations')  # Field name made lowercase.
    randomphrase = models.TextField(db_column='randomPhrase')  # Field name made lowercase.
    personalquote = models.TextField(db_column='personalQuote')  # Field name made lowercase.

