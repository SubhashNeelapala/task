from django.db import models

# Create your models here.
class Team(models.Model):
	name = models.CharField(max_length=100,unique=True)
	logo = models.ImageField(upload_to='Team',blank=True,null=True)
	club_state = models.CharField(max_length=100,blank=True,null=True)
	def __str__(self):
		return '%s' % self.name

class Player(models.Model):
	firstname = models.CharField(max_length=100,blank=True,null=True)
	lastname = models.CharField(max_length=100,blank=True,null=True)
	image = models.ImageField(upload_to='Player',blank=True,null=True)
	player_jersey_no = models.CharField(max_length=100,unique=True)
	country	= models.CharField(max_length=100,blank=True,null=True)
	player_team = models.ForeignKey(Team, blank=True, null=True)
	no_matches = models.CharField(max_length=100,blank=True,null=True)
	no_runs = models.CharField(max_length=100,blank=True,null=True)
	highest_scores= models.CharField(max_length=100,blank=True,null=True)
	no_fifties = models.CharField(max_length=100,blank=True,null=True)
	no_hundreds = models.CharField(max_length=100,blank=True,null=True)

	def __str__(self):
		return '%s' % self.player_jersey_no

class Matches(models.Model):
	contestant1 =  models.ForeignKey(Team,related_name='matches_winner_contestant1')
	contestant2 =  models.ForeignKey(Team,related_name='matches_winner_contestant2')

class Points(models.Model):
	match = models.ForeignKey(Matches)
	winner = models.CharField(max_length=100,blank=True,null=True)
	contestant1_points = models.CharField(max_length=100,blank=True,null=True)
	contestant2_points = models.CharField(max_length=100,blank=True,null=True)