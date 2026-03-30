from django.core.management.base import BaseCommand
from octofit_tracker.models.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            Leaderboard.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            users = [
                User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
                User(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
                User(name='Batman', email='batman@dc.com', team=dc),
            ]
            for user in users:
                user.save()

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, date='2023-01-01')
            Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, date='2023-01-02')
            Activity.objects.create(user=users[2], activity_type='Swimming', duration_minutes=60, date='2023-01-03')
            Activity.objects.create(user=users[3], activity_type='Yoga', duration_minutes=50, date='2023-01-04')

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            w1 = Workout.objects.create(name='Full Body Blast', description='A full body workout')
            w2 = Workout.objects.create(name='Cardio Burn', description='High intensity cardio')
            w1.suggested_for.set([users[0], users[2]])
            w2.suggested_for.set([users[1], users[3]])

            self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
            Leaderboard.objects.create(team=marvel, total_points=100, rank=1)
            Leaderboard.objects.create(team=dc, total_points=90, rank=2)

            self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
