
# import csv
# from django.core.management.base import BaseCommand
# from django.db import transaction
# from ipl.models import Matches

# class Command(BaseCommand):
#     '''Import data from CSV file into MyModel using functional transactions'''

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file', type=str, help='Path to the CSV file')

#     def handle(self, *args, **options):
#         csv_file_path = options['csv_file']

#         try:
#             with transaction.atomic():
#                 # Open the CSV file and read data
#                 with open(csv_file_path, 'r') as csv_file:
#                     csv_reader = csv.reader(csv_file)
#                     next(csv_reader)  # Skip header row if present

#                     # Iterate over rows and create MyModel instances
#                     for row in csv_reader:
#                         Matches.objects.create(
#                             id = int(row[0]),
#                             season	= int(row[1]),
#                             city = row[2],	
#                             date = row[3],
#                             team1 = row[4], 	
#                             team2 = row[5],	
#                             toss_winner	= row[6],
#                             toss_decision = row[7], 
#                             result = row[8],
#                             dl_applied = int(row[9]),                            
#                             winner =  row[10],
#                             win_by_runs	= int(row[11]),
#                             win_by_wickets = int(row[12]),
#                             player_of_match	= row[13],
#                             venue =row[14],
#                             umpire1	= row[15],
#                             umpire2 = row[16],
#                             # Add more fields as needed
#                         )

#                 self.stdout.write(self.style.SUCCESS('Data import successful.'))

#         except Exception as e:
#             self.stdout.write(self.style.ERROR(f'Data import failed. {str(e)}'))





import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.db import transaction
from ipl.models import Matches, Deliveries
from django.apps import apps
class Command(BaseCommand):
    '''Import data from CSV file into MyModel using functional transactions'''

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Model name')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        model_name = options['model_name']
        try:
            with open(csv_file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                model = apps.get_model('ipl', model_name)
                
                fields = csv_reader.fieldnames
                data_to_import = []
                for row in csv_reader:
                    instance_data = {field: row.get(field) for field in fields}
                    data_to_import.append(instance_data)
                
                with transaction.atomic():
                    for data in data_to_import:
                        if 'date' in data:
                            data['date'] = datetime.strptime(row['date'], '%Y-%m-%d').date()
                        if model == Deliveries:
                            if 'match_id' in data:
                                match_id = int(data.pop('match_id'))
                                data['match_id'] = Matches.objects.get(id=match_id)                  
                        instace = model(**data)
                        instace.save()
            self.stdout.write(self.style.SUCCESS('Data import successful.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Data import failed. {str(e)}'))



# import_data.py
# import csv
# from django.core.management.base import BaseCommand
# from django.db import transaction
# from ipl.models import Match, Inning

# class Command(BaseCommand):
    
    # FIELD_MAPPING_MATCH = {
    #     'id': 'id',
    #     'season': 'season',
    #     'city': 'city',
    #     'date': 'date',
    #     'team1': 'team1',
    #     'team2': 'team2',
    #     'toss_winner': 'toss_winner',
    #     'toss_decision': 'toss_decision',
    #     'result': 'result',
    #     'dl_applied': 'dl_applied',
    #     'winner': 'winner',
    #     'win_by_runs': 'win_by_runs',
    #     'win_by_wickets': 'win_by_wickets',
    #     'player_of_match': 'player_of_match',
    #     'venue': 'venue',
    #     'umpire1': 'umpire1',
    #     'umpire2': 'umpire2',
    # }

    # FIELD_MAPPING_INNING = {
    #     'inning': 'inning',
    #     'batting_team': 'batting_team',
    #     'bowling_team': 'bowling_team',
    #     'over': 'over',
    #     'ball': 'ball',
    #     'batsman': 'batsman',
    #     'non_striker': 'non_striker',
    #     'bowler': 'bowler',
    #     'is_super_over': 'is_super_over',
    #     'wide_runs': 'wide_runs',
    #     'bye_runs': 'bye_runs',
    #     'legbye_runs': 'legbye_runs',
    #     'noball_runs': 'noball_runs',
    #     'penalty_runs': 'penalty_runs',
    #     'batsman_runs': 'batsman_runs',
    #     'extra_runs': 'extra_runs',
    #     'total_runs': 'total_runs',
    #     'player_dismissed': 'player_dismissed',
    #     'dismissal_kind': 'dismissal_kind',
    #     'fielder': 'fielder',
    # }

    
    # help = 'Import data from CSV files into Match and Inning models using functional transactions'

    # def add_arguments(self, parser):
    #     parser.add_argument('match_csv', type=str, help='Path to the CSV file for Match model')
    #     parser.add_argument('inning_csv', type=str, help='Path to the CSV file for Inning model')

    # def handle(self, *args, **options):
    #     match_csv_file_path = options['match_csv']
    #     inning_csv_file_path = options['inning_csv']

    #     try:
    #         with open(match_csv_file_path, 'r') as match_csv_file:
    #             match_csv_reader = csv.DictReader(match_csv_file)
    #             matches_to_create = []
                
    #             fields = match_csv_reader.fieldnames
    #             print(fields)

    #             # Process Match data
    #             for row in match_csv_reader:
    #                 # match_data = {model_field: row[csv_field] for csv_field, model_field in Command.FIELD_MAPPING_MATCH.items()}
    #                 match_data = {csv_field: row[csv_field] for csv_field in fields}
        #             match_instance = Match(**match_data)
        #             matches_to_create.append(match_instance)

        #         with transaction.atomic():
        #             # Bulk create Match instances
        #             Match.objects.bulk_create(matches_to_create)

        #     with open(inning_csv_file_path, 'r') as inning_csv_file:
        #         inning_csv_reader = csv.DictReader(inning_csv_file)
        #         innings_to_create = []
                
        #         fields = inning_csv_reader.fieldnames
                
        #         # Process Inning data
        #         for row in inning_csv_reader:
        #             inning_data = {csv_field: row[csv_field] for csv_field in fields}
        #             # inning_data = {model_field: row[csv_field] for csv_field, model_field in Command.FIELD_MAPPING_INNING.items()}
        #             match_id = row['match_id']
        #             # Retrieve the corresponding Match instance based on match_id
        #             match_instance = Match.objects.get(id=match_id)
        #             inning_data['match_id'] = match_instance
        #             inning_instance = Inning(**inning_data)
        #             innings_to_create.append(inning_instance)

        #         with transaction.atomic():
        #             # Bulk create Inning instances
        #             Inning.objects.bulk_create(innings_to_create)

        #     self.stdout.write(self.style.SUCCESS('Data import successful.'))

        # except Exception as e:
        #     self.stdout.write(self.style.ERROR(f'Data import failed. {e}'))

   