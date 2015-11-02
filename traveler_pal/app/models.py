# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from DjangoUeditor.models import UEditorField

currentDateTime = timezone.now()
nameFieldMaxSize = 128


# Create your models here.
class Scenery(models.Model):
    name = models.CharField(max_length=nameFieldMaxSize, null=True)
    price = models.IntegerField(null=True)


class Activity(models.Model):
    """
    """
    name = models.CharField(max_length=nameFieldMaxSize)
    launchedDateTime = models.DateTimeField(default=currentDateTime, null=True)
    startDateTime = models.DateTimeField(default=currentDateTime, null=True)
    endDateTime = models.DateTimeField(default=currentDateTime, null=True)
    scenerys = models.ManyToManyField(Scenery, through="ActivityScenery")


class ActivityScenery(models.Model):
    activity = models.ForeignKey(Activity, null=True)
    scenery = models.ForeignKey(Scenery, null=True)


class Person(models.Model):
    """
    """
    # info
    user = models.ForeignKey(User, null=True)
    username = models.CharField(max_length=nameFieldMaxSize, null=True)
    email = models.EmailField(max_length=nameFieldMaxSize, null=True)
    password = models.CharField(max_length=nameFieldMaxSize, null=True)
    interest = models.TextField(null=True)
    gender = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )

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
    # joinedDateTime = models.DateTimeField(default=currentDateTime, null=True) #current no usage
    # more user info


class PersonScenery(models.Model):
    person = models.ForeignKey(Person, null=True)
    scenery = models.ForeignKey(Scenery, null=True)


class Postable(models.Model):
    person = models.ForeignKey(Person)
    title = models.CharField(max_length=nameFieldMaxSize)
    content = models.TextField(null=True)
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
    only
    """
    activity = models.ForeignKey(Activity, null=True)

class Blog(models.Model):
    title=models.CharField(max_length=100,blank=True)
    content = UEditorField(imagePath="ueditor/images/", filePath="ueditor/files/", settings={},command=None,blank=True)