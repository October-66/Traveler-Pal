from django.db import models
from django.utils import timezone

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

    activitys = models.ManyToManyField(Activity, through="UserActivity")
    scenerys = models.ManyToManyField(Scenery, through="UserScenery")

    def __str__(self):
        return "user named %s with all stuff" % self.username


class UserActivity(models.Model):
    """
    a membership between act and user
    user can get activity joined by `activity_set` in shell
    """
    user = models.ForeignKey(User, null=True)
    activity = models.ForeignKey(Activity, null=True)
    # joinedDateTime = models.DateTimeField(default=currentDateTime, null=True) #current no usage
    # more user info


class UserScenery(models.Model):
    user = models.ForeignKey(User, null=True)
    scenery = models.ForeignKey(Scenery, null=True)


class Postable(models.Model):
    user = models.ForeignKey(User)
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
