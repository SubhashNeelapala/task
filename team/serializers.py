from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=100)
	club_state = serializers.CharField(max_length=100)

class PlayerSerializer(serializers.Serializer):
	firstname = serializers.CharField(max_length=100)
	lastname = serializers.CharField(max_length=100)
	jersey_no = serializers.CharField(max_length=100)
	country = serializers.CharField(max_length=100)
	team_id = serializers.CharField(max_length=100)

class MatchCreateSerializer(serializers.Serializer):
	contestant1 = serializers.CharField()
	contestant2 = serializers.CharField()

class CreatPointsWinnerSerializer(serializers.Serializer):
	match=serializers.CharField(max_length=100)
	winner=serializers.CharField(max_length=100)
	contestant1_points=serializers.CharField(max_length=100)
	contestant2_points=serializers.CharField(max_length=100)

