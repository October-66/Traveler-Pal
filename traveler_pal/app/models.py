from django.db import models

# Create your models here.
nameFieldMaxSize = 128


class User(models.Model):
    """
    """
    username = models.CharField(max_length=nameFieldMaxSize)
    email = models.EmailField(max_length=nameFieldMaxSize)
    password = models.CharField(max_length=nameFieldMaxSize)
    # more info

    # keys


class Activity(models.Model):
    """
    """
    name = models.CharField(max_length=nameFieldMaxSize)
    # launchedDate = models.DateField()

    members = models.ManyToManyField(User, through="ActivityUser")
    # scenerys = models.ManyToManyField(Scenery, through="ActivityScenery")


class ActivityUser(models.Model):
    """
    a membership between act and user
    """
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)
    # joinedDate = models.DateTimeField()
    # more user info


class Scenery(models.Model):
    """
    """


class ActivityScenery(models.Model):
    """
    """


class Comment(models.Model):
    """
    """


class SceneryComment(models.Model):
    """
    """


class UserComment(models.Model):
    """
    """


class Journal(models.Model):
    """
    """


class UserJournal(models.Model):
    """
    """
