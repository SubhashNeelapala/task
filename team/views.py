from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from .models import *
from .serializers import *
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.db import IntegrityError

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
class TeamListViewSet(APIView):
		
		def get(self, request, format=None):
			team_obj_list = Team.objects.values('name','logo','club_state','id')
			context_data = {"success":True,"data":team_obj_list}
			return Response(context_data)
		@method_decorator(csrf_exempt)
		def post(self, request,format=None):
				serializer = TeamSerializer(data=json.loads(request.data['data']))
				user_data = json.loads(request.data['data'])
				if serializer.is_valid():
						try:
								team_form = {
														"name": user_data['name'],
														"club_state": user_data['club_state']              
														}

								if 'image' in request.data:
										if request.data['image']:
												team_form.update({"logo" : request.data['image']})
								
								try:
										Team.objects.create(**team_form)
										context_data = {"success" : True,"message" : "Record Created Successfully"}
								except IntegrityError as e:
										# print (e)
										context_data = {"success" : False,"errors" : {"message":str(e)}}
						except Exception as e:
							context_data = {"success" : False, "errors" : {"message":str(e)}}
				else:
						context_data = {"success" : False, "errors" : {"message": "Validation Error" ,  "errors_list" : serializer.errors}}            
				return Response(context_data)




class PlayerListViewSet(APIView):
	def post(self,request,format=None):
		serializer = PlayerSerializer(data=json.loads(request.data['data']))
		player_request=json.loads(request.data['data'])
		if serializer.is_valid():

			try:
				team_obj = Team.objects.get(pk=player_request['team_id'])
			except Team.DoesNotExist as e:
				context_data = {"success" : False, "errors" : {"message":"Team does not exist"}}
			
			player_form = {
			"firstname":player_request['firstname'],
			"lastname":player_request['lastname'],
			"player_jersey_no":player_request['jersey_no'],
			"country":player_request['country'],
			"player_team":team_obj,
			"image":request.data['image']
			}

			try:
				Player.objects.create(**player_form)
				context_data = {"success" : True,"message" : "Player Created Successfully"}
			except Exception as e:
				context_data ={"success":False,"errors":{"message":str(e)}}
		else:
			context_data = {"success":False, "errors" : {"message": "Validation Error" ,  "errors_list" : serializer.errors}}
		return Response(context_data)

class PlayerListByTeam(APIView):
	def get(self,request,format=None,team_id=None):
		try:
			team_obj = Team.objects.get(pk=team_id)
		except Team.DoesNotExist as e:
			context_data = {"success" : False, "errors" : {"message":"Team does not exist"}}
		player_list = Player.objects.filter(player_team=team_obj).values('firstname','lastname','image','player_jersey_no','country','no_matches','no_runs','highest_scores','no_fifties','no_hundreds')
		context_data = {"success":True,"data":player_list}
		return Response(context_data)

class MatchCreateViewSet(APIView):
	def post(self,request,format=None):
		serializer = MatchCreateSerializer(data=request.data)
		if serializer.is_valid():
			try:
				team1_obj = Team.objects.get(pk=request.data['contestant1'])
			except Team.DoesNotExist as e:
				context_data = {"success" : False, "errors" : {"message":"Team does not exist"}}

			try:
				team2_obj = Team.objects.get(pk=request.data['contestant2'])
			except Team.DoesNotExist as e:
				context_data = {"success" : False, "errors" : {"message":"Team does not exist"}}

			match_form = {
			"contestant1" : team1_obj,
			"contestant2" : team2_obj
			}

			try:
				Matches.objects.create(**match_form)
				context_data = {"success" : True,"message" : "Match Created Successfully for {} and {}".format(team1_obj.name,team2_obj.name)}
			except Exception as e:
				context_data = {"success" : False, "errors" : {"message":str(e)}}
		else:
			context_data = {"success" : False, "errors" : {"message": serializer.errors}}

		return Response(context_data)

class MatchesListViewSet(APIView):
	def get(self,request):
		matches_list = Matches.objects.values('contestant1__name','contestant2__name','id')
		if matches_list:
			context_data = {"success":True,"data":matches_list}
		else:
			context_data = {"success":True,"messgae":"No matches found"}
		return Response(context_data)

class CreatPointWinnerMatches(APIView):
	def get(self,request,format=None):
		match_points_list = Points.objects.values("match__contestant1__name","match__contestant2__name","contestant1_points","contestant2_points")
		context_data ={"success":True,"data":match_points_list}
		return Response(context_data)

	def post(self,request,format=None):
		serializers = CreatPointsWinnerSerializer(data=request.data)
		if serializers.is_valid():
			try:
				match_obj = Matches.objects.get(pk=request.data['match'])	
			except Matches.DoesNotExist as e:
				context_data = {"success" : False, "errors" : {"message":"Matches does not exist"}}

			winner_form = {
			"match":match_obj,
			"winner":request.data['winner'],
			"contestant1_points":request.data['contestant1_points'],
			"contestant2_points":request.data['contestant2_points']
			}
			try:
				Points.objects.create(**winner_form)
				context_data = {"success" : True, "message" :"Match Details Updated"}
			except Exception as e:
				context_data = {"success" : False, "errors" : {"message":str(e)}}
		else:
			context_data = {"success" : False, "errors" : {"message":serializer.errors}}
		return Response(context_data)

