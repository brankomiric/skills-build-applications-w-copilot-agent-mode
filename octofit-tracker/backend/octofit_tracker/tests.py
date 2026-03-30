from django.test import TestCase
from rest_framework.test import APIClient
from .models.models import User, Team, Activity, Workout, Leaderboard
from django.urls import reverse
from datetime import date

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Team A", description="Test team")
        self.user = User.objects.create(name="John Doe", email="john@example.com", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration_minutes=30, date=date.today())
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)

    def test_api_root(self):
        response = self.client.get(reverse('api_root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_user_list(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_team_list(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activity_list(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workout_list(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard_list(self):
        response = self.client.get('/leaderboards/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
