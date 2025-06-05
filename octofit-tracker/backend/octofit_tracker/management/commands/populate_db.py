from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='thundergod', password='thundergodpassword'),
            User(email='metalgeek@mhigh.edu', name='metalgeek', password='metalgeekpassword'),
            User(email='zerocool@mhigh.edu', name='zerocool', password='zerocoolpassword'),
            User(email='crashoverride@hmhigh.edu', name='crashoverride', password='crashoverridepassword'),
            User(email='sleeptoken@mhigh.edu', name='sleeptoken', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()
        for user in users:
            team1.members.add(user)
            team2.members.add(user)

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60, date='2025-06-01', points=10),
            Activity(user=users[1], activity_type='Crossfit', duration=120, date='2025-06-02', points=20),
            Activity(user=users[2], activity_type='Running', duration=90, date='2025-06-03', points=15),
            Activity(user=users[3], activity_type='Strength', duration=30, date='2025-06-04', points=8),
            Activity(user=users[4], activity_type='Swimming', duration=75, date='2025-06-05', points=12),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, total_points=100),
            Leaderboard(team=team2, total_points=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', difficulty='Medium'),
            Workout(name='Crossfit', description='Training for a crossfit competition', difficulty='Hard'),
            Workout(name='Running Training', description='Training for a marathon', difficulty='Medium'),
            Workout(name='Strength Training', description='Training for strength', difficulty='Easy'),
            Workout(name='Swimming Training', description='Training for a swimming competition', difficulty='Medium'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
