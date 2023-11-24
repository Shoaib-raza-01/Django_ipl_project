from django.urls import path
from . import views

app_name = 'ipl'

urlpatterns = [
    path('', views.index, name='index'),
    path('ques-1/', views.question_one, name='matches-per-year'),
    path('ques-2/', views.question_two, name='count_per_season_per_team'),
    path('ques-3/', views.question_three, name='extra-runs-conceded'),
    path('ques-4/', views.question_four, name="question-four"),
    
    path('ques-1/chart', views.matches_per_year, name="matches-per-year_chart"),
    path('ques-2/chart', views.count_per_season_per_team, name="count_per_season_per_team_chart"),
    path('ques-3/chart', views.extra_runs_conceded, name="extra-runs-conceded-chart"),
    path('ques-4/chart', views.top_economical_bowler, name='top-economical-bowler_chart'),
]