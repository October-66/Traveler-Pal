from django.db import models

# Create your models here.
class Comment(models.Model):
    """
    made by user, apply to scenery
    """
    content = models.TextField()


nameFieldMaxSize = 128

class Journal(models.Model):
    """
    only
    """
    title = models.CharField(nameFieldMaxSize)
    content = models.TextField()


class User(models.Model):
    """
    """
    #base info
    username = models.CharField(max_length=nameFieldMaxSize)
    email = models.EmailField(max_length=nameFieldMaxSize)
    password = models.CharField(max_length=nameFieldMaxSize)
    # more info
    interest = models.TextField()
    gender = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )

    # keys
    comments = models.ManyToManyField(Comment, through="UserComment")
    journals = models.ManyToManyField(Journal, through="UserJournal")


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
    name = models.CharField(nameFieldMaxSize)
    price = models.DecimalField()

    comments = models.ManyToManyField(Comment, through="SceneryComment")



class Activity(models.Model):
    """
    """
    name = models.CharField(max_length=nameFieldMaxSize)
    launchedDate = models.DateField()
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()

    members = models.ManyToManyField(User, through="ActivityUser")
    scenerys = models.ManyToManyField(Scenery, through="ActivityScenery")


class ActivityUser(models.Model):
    """
    a membership between act and user
    user can get activity joined by `activity_set` in shell
    """
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity)
    joinedDate = models.DateField()

    # more user info


class ActivityScenery(models.Model):
    activity = models.ForeignKey(Activity)
    scenery = models.ForeignKey(Scenery)



class SceneryComment(models.Model):
    scenery = models.ForeignKey(Scenery)
    comment = models.ForeignKey(Comment)
