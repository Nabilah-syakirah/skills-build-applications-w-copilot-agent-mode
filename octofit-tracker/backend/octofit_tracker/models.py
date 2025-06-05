from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    # Add additional fields as needed

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()
    points = models.IntegerField(default=0)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
