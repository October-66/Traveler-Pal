from django.db import models
from django.utils import timezone

currentDateTime = timezone.now()
nameFieldMaxSize = 128


# Create your models here.
class Comment(models.Model):
    """
    made by user, apply to scenery
    """
    content = models.TextField()


class Journal(models.Model):
    """
    only
    """
    title = models.CharField(max_length=nameFieldMaxSize)
    content = models.TextField()


class UserInfo(models.Model):
    username = models.CharField(max_length=nameFieldMaxSize)
    email = models.EmailField(max_length=nameFieldMaxSize)
    password = models.CharField(max_length=nameFieldMaxSize)
    interest = models.TextField()
    gender = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )

    def __str__(self):
        return "%s's base information" % self.username


class User(models.Model):
    """
    """
    info = models.OneToOneField(UserInfo)

    # keys
    comments = models.ManyToManyField(Comment, through="UserComment")
    journals = models.ManyToManyField(Journal, through="UserJournal")

    def __str__(self):
        return "the user with all stuff"


class UserComment(models.Model):
    """
    an intermediary between user and comment
    """
    user = models.ForeignKey(User)
    Comment = models.ForeignKey(Comment)


class UserJournal(models.Model):
    user = models.ForeignKey(User)
    journal = models.ForeignKey(Journal)


class Scenery(models.Model):
    name = models.CharField(max_length=nameFieldMaxSize)
    price = models.IntegerField()

    comments = models.ManyToManyField(Comment, through="SceneryComment")


class SceneryComment(models.Model):
    scenery = models.ForeignKey(Scenery)
    comment = models.ForeignKey(Comment)


class Activity(models.Model):
    """
    """
    name = models.CharField(max_length=nameFieldMaxSize)
    # launchedDate = models.DateField(default=currentDateTime)
    # startDateTime = models.DateTimeField(default=currentDateTime)
    # endDateTime = models.DateTimeField(default=currentDateTime)

    users = models.ManyToManyField(User, through="ActivityUser")
    scenerys = models.ManyToManyField(Scenery, through="ActivityScenery")


class ActivityUser(models.Model):
    """
    a membership between act and user
    user can get activity joined by `activity_set` in shell
    """
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)
    # joinedDate = models.DateField(default=currentDateTime)
    # more user info


class ActivityScenery(models.Model):
    activity = models.ForeignKey(Activity)
    scenery = models.ForeignKey(Scenery)
