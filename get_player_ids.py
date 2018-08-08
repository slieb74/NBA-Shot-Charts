import requests
import pandas as pd
from all_players_list import players_list
#import matplotlib.pyplot as plt

players_index_url = 'https://stats.nba.com/players/list/'
player_page_url_base = 'https://stats.nba.com/player/'
players_json = 'https://stats.nba.com/js/data/ptsd/stats_ptsd.js'

shot_chart_url_start= 'https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&CFPARAMS=2017-18&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID='
shot_chart_url_end= '&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID='

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

players_list = players_list

rookies = [player[0:5] for player in players_list if player[3]==2018]
vets = [player[0:5] for player in players_list if player[4]==2018 and player[3]!=2018]

vets_df = pd.DataFrame(vets, columns=['ID', 'Name', 'Active', 'RookieYear', 'LastSeasonPlayed'])
vets_df = vets_df.drop(columns=['Active', 'RookieYear', 'LastSeasonPlayed'])

player_ids = [player[0] for player in vets]

def find_player_id(last_name_comma_first_name):
    return vets_df.loc[vets_df.Name==last_name_comma_first_name].iloc[0]['ID']

def get_shot_data(player_id):
    full_url = shot_chart_url_start + str(player_id) + shot_chart_url_end
    json = requests.get(full_url, headers=headers).json()
    return(json)

# json = get_shot_data(204001)
#
# # def get_all_players_shot_data(player_ids):
# #     all_shots = []
# #     for id in player_ids:
# #         all_shots.append(get_shot_data(id))
# #     return all_shots
# # all_players_sample = player_ids[100:105]
# # all_json = get_all_players_shot_data(all_players_sample)
#
data = json['resultSets'][0]['rowSet']
columns = json['resultSets'][0]['headers']
league_avgs = json['resultSets'][1]['rowSet']
league_avg_columns = json['resultSets'][1]['headers']

league_avgs_df = pd.DataFrame.from_records(league_avgs, columns=league_avg_columns)

df = pd.DataFrame.from_records(data, columns=columns)

columns_to_drop = ['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'GAME_DATE', 'HTM', 'VTM']

df = df.drop(columns=columns_to_drop)
