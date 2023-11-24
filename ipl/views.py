from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from . import models
import requests
import json
# from django.db.models import Count
import django.db.models as m

# Create your views here.


def index(request):
    return render(request, 'ipl/index.html')

def question_one(request):
    instance = models.Matches.objects.values('season').annotate(
        count = m.Count('id')
    ).order_by('season')
    return JsonResponse(list(instance), safe=False)

def question_two(request):
    instance = models.Matches.objects.values('season','winner').annotate(
        count = m.Count('id')
    ).order_by(
        'season','winner'
    )
    
    data = {}
    for item in instance:   
        if item['season'] in data:
            data[item['season']][item['winner']] = item['count']
        else:
            data[item['season']] = {item['winner']: item['count']}
    return JsonResponse(data, safe=False)

def question_three(request):
    instance = models.Deliveries.objects.filter(match_id__season=2016).values('bowling_team').annotate(
        runs_conceded = m.Sum('extra_runs')
    ).order_by('bowling_team')
    
    return JsonResponse(list(instance), safe=False)

def question_four(request):
    instance = models.Deliveries.objects.filter(match_id__season=2015).values('bowler').annotate(
        economy = m.Sum('total_runs')/(m.Count('bowler')/6.0)
        # total_runs = m.Sum('total_runs'),
        # total_balls = m.Count('bowler')
    ).order_by('economy')[:10]
    return JsonResponse(list(instance), safe=False)

def matches_per_year(request):
    path = request.build_absolute_uri(reverse("ipl:matches-per-year"))
    response = requests.get(path)
    data = response.json()
    context = {
        'data' : json.dumps(data)
    }
    return render(request, 'ipl/matches_per_year.html', context)

def count_per_season_per_team(request):
    path = request.build_absolute_uri(reverse("ipl:count_per_season_per_team"))
    response = requests.get(path)
    data = response.json()
    
    years = list(data.keys())
    # teams = list(data['2011'].keys())
        
    teams_query =models.Matches.objects.values('team1').order_by('team1').distinct()
    list_of_teams = list(teams_query)
    teams = [team['team1'] for team in list_of_teams]
    # print(teams)
    
    series = []
    for team in teams:
        team_data = [data[year].get(team, 0) for year in years]
        series.append({"name": team, "data": team_data})

    context = {"teams": teams, "years": years, "series": series}
    return render(request, "ipl/win_per_season_per_team.html", context)

def extra_runs_conceded(request):
    path = request.build_absolute_uri(reverse("ipl:extra-runs-conceded"))
    response = requests.get(path)
    data = response.json()
    context = {
        'data' : json.dumps(data)
    }
    return render(request, 'ipl/extra_run_conceded.html', context) 


def top_economical_bowler(request):
    path = request.build_absolute_uri(reverse("ipl:question-four"))
    response = requests.get(path)
    data = response.json()
    context = {
        'data' : json.dumps(data)
    }
    return render(request, 'ipl/economical_bowler.html', context) 




