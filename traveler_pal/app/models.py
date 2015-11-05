# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField

currentDateTime = timezone.now()
nameFieldMaxSize = 128


class Scenery(models.Model):
    name = models.CharField(max_length=nameFieldMaxSize, null=True)
    price = models.IntegerField(null=True)

    def ___str__(self):
        return "scenery name: " + self.name


class Activity(models.Model):
    """
    """
    name = models.CharField(max_length=nameFieldMaxSize)
    launchedDateTime = models.DateTimeField(default=currentDateTime, null=True)
    startDateTime = models.DateTimeField(default=currentDateTime, null=True)
    endDateTime = models.DateTimeField(default=currentDateTime, null=True)
    introduction = models.CharField(default="", max_length=nameFieldMaxSize)
    sponsor = models.CharField(default="", max_length=nameFieldMaxSize)
    scenerys = models.ManyToManyField(Scenery, through="ActivityScenery")

    def __str__(self):
        return "activity name: " + self.name


class ActivityScenery(models.Model):
    activity = models.ForeignKey(Activity, null=True)
    scenery = models.ForeignKey(Scenery, null=True)


class Person(models.Model):
    """
    """
    #User in Django contains email, name, username, password(cannot be seen)
    user = models.ForeignKey(User, null=True)

    username = models.CharField(max_length=nameFieldMaxSize, null=True) #to identify user and avoid get User fk
    interest = models.TextField(null=True)
    genderChoices = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    gender = models.CharField(max_length=1, choices=genderChoices, default='M')
    activitys = models.ManyToManyField(Activity, through="PersonActivity")
    scenerys = models.ManyToManyField(Scenery, through="PersonScenery")

    def __str__(self):
        return "user named %s with all stuff" % self.username


class PersonActivity(models.Model):
    """
    a membership between act and user
    user can get activity joined by `activity_set` in shell
    """
    person = models.ForeignKey(Person, null=True)
    activity = models.ForeignKey(Activity, null=True)

    joinedDateTime = models.DateTimeField(default=currentDateTime, null=True)
    # more user info


class PersonScenery(models.Model):
    person = models.ForeignKey(Person, null=True)
    scenery = models.ForeignKey(Scenery, null=True)


class Postable(models.Model):
    person = models.ForeignKey(Person, null=True)
    title = models.CharField(max_length=nameFieldMaxSize)
    content = UEditorField(imagePath="ueditor/images/",
                           filePath="ueditor/files/", settings={}, command=None, blank=True)
    postDateTime = models.DateTimeField(default=currentDateTime, null=True)

    class meta:
        abstract = True


class Comment(Postable):
    """
    made by user, apply to scenery
    """
    scenery = models.ForeignKey(Scenery, null=True)


class Journal(Postable):
    """
    only can be seen by user himself
    """
    activity = models.ForeignKey(Activity, null=True)


class Strategy(Postable):
    """
    can be seen by everyone and post on homepage
    """
    acitvity = models.ForeignKey(Activity, null=True)
