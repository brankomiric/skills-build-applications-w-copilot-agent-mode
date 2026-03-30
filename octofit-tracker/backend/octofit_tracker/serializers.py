from rest_framework import serializers
from .models.models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId

# Helper to convert ObjectId to string
def to_str(obj):
    return str(obj) if isinstance(obj, ObjectId) else obj

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']
    def get_id(self, obj):
        return to_str(obj.id)

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = TeamSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'is_active']
    def get_id(self, obj):
        return to_str(obj.id)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'date']
    def get_id(self, obj):
        return to_str(obj.id)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    suggested_for = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']
    def get_id(self, obj):
        return to_str(obj.id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'total_points', 'rank']
    def get_id(self, obj):
        return to_str(obj.id)
