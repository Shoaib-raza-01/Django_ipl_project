from django.db import models

# Create your models here.

class Matches(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    season = models.IntegerField()
    city = models.CharField(max_length=30)
    date = models.DateField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)	
    toss_winner	= models.CharField(max_length=50)
    toss_decision = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    dl_applied = models.IntegerField()
    winner = models.CharField(max_length=50)
    win_by_runs	= models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match	= models.CharField(max_length=30)
    venue = models.CharField(max_length=100)
    umpire1	= models.CharField(max_length=50)
    umpire2	= models.CharField(max_length=50)
    
    def __str__(self):
        return self.winner
    
class Deliveries(models.Model):
    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=50)
    bowling_team = models.CharField(max_length=50)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman	= models.CharField(max_length=50)
    non_striker	= models.CharField(max_length=50)
    bowler = models.CharField(max_length=50)
    is_super_over = models.BooleanField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs	= models.IntegerField()
    noball_runs	= models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=30)
    dismissal_kind = models.CharField(max_length=30)
    fielder = models.CharField(max_length=30)




# # models.py
# from django.db import models

# class Match(models.Model):
#     id = models.IntegerField(primary_key=True)
#     season = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     date = models.DateField()
#     team1 = models.CharField(max_length=100)
#     team2 = models.CharField(max_length=100)
#     toss_winner = models.CharField(max_length=100)
#     toss_decision = models.CharField(max_length=10)
#     result = models.CharField(max_length=100)
#     dl_applied = models.BooleanField()
#     winner = models.CharField(max_length=100)
#     win_by_runs = models.IntegerField()
#     win_by_wickets = models.IntegerField()
#     player_of_match = models.CharField(max_length=100)
#     venue = models.CharField(max_length=100)
#     umpire1 = models.CharField(max_length=100)
#     umpire2 = models.CharField(max_length=100)

#     def __str__(self):
#         return f"Match ID: {self.id}, Teams: {self.team1} vs {self.team2}"

# class Inning(models.Model):
#     match_id = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='innings')
#     inning = models.IntegerField()
#     batting_team = models.CharField(max_length=100)
#     bowling_team = models.CharField(max_length=100)
#     over = models.IntegerField()
#     ball = models.IntegerField()
#     batsman = models.CharField(max_length=100)
#     non_striker = models.CharField(max_length=100)
#     bowler = models.CharField(max_length=100)
#     is_super_over = models.BooleanField()
#     wide_runs = models.IntegerField()
#     bye_runs = models.IntegerField()
#     legbye_runs = models.IntegerField()
#     noball_runs = models.IntegerField()
#     penalty_runs = models.IntegerField()
#     batsman_runs = models.IntegerField()
#     extra_runs = models.IntegerField()
#     total_runs = models.IntegerField()
#     player_dismissed = models.CharField(max_length=100, null=True, blank=True)
#     dismissal_kind = models.CharField(max_length=100, null=True, blank=True)
#     fielder = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return f"Inning ID: {self.id}, Match ID: {self.match_id}, Batting Team: {self.batting_team}"
# 