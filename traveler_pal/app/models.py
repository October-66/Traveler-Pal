from django.db import models
from django.utils import timezone

currentDateTime = timezone.now()
nameFieldMaxSize = 128


# Create your models here.
class Comment(models.Model):
    """
    made by user, apply to scenery
    """
    content = models.TextField(null=True)


class Journal(models.Model):
    """
    only
    """
    title = models.CharField(max_length=nameFieldMaxSize, null=True)
    content = models.TextField(null=True)


class User(models.Model):
    """
    """
    # info
    username = models.CharField(max_length=nameFieldMaxSize, null=True)
    email = models.EmailField(max_length=nameFieldMaxSize, null=True)
    password = models.CharField(max_length=nameFieldMaxSize, null=True)
    interest = models.TextField(null=True)
    gender = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )

    # keys
    comments = models.ManyToManyField(Comment, through="UserComment")
    journals = models.ManyToManyField(Journal, through="UserJournal")

    def __str__(self):
        return "user named %s with all stuff" % self.username


class UserComment(models.Model):
    """
    an intermediary between user and comment
    """
    user = models.ForeignKey(User, null=True)
    Comment = models.ForeignKey(Comment, null=True)


class UserJournal(models.Model):
    user = models.ForeignKey(User, null=True)
    journal = models.ForeignKey(Journal, null=True)


class Scenery(models.Model):
    name = models.CharField(max_length=nameFieldMaxSize, null=True)
    price = models.IntegerField(null=True)

    comments = models.ManyToManyField(Comment, through="SceneryComment")


class SceneryComment(models.Model):
    scenery = models.ForeignKey(Scenery, null=True)
    comment = models.ForeignKey(Comment, null=True)


class Activity(models.Model):
    """
    """
    name = models.CharField(max_length=nameFieldMaxSize)
    launchedDate = models.DateField(default=currentDateTime, null=True)
    startDateTime = models.DateTimeField(default=currentDateTime, null=True)
    endDateTime = models.DateTimeField(default=currentDateTime, null=True)

    users = models.ManyToManyField(User, through="ActivityUser")
    scenerys = models.ManyToManyField(Scenery, through="ActivityScenery")


class ActivityUser(models.Model):
    """
    a membership between act and user
    user can get activity joined by `activity_set` in shell
    """
    user = models.ForeignKey(User, null=True)
    activity = models.ForeignKey(Activity, null=True)
    joinedDate = models.DateField(default=currentDateTime, null=True)
    # more user info


class ActivityScenery(models.Model):
    activity = models.ForeignKey(Activity, null=True)
    scenery = models.ForeignKey(Scenery, null=True)
