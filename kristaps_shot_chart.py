import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='slieb74', api_key='eNqli0rVtoX1YAUXDhcr')
import pandas as pd
from court import court_shapes
from get_player_ids import *

players_list = players_list
vets = [player[0:5] for player in players_list if player[4]==2018 and player[3]!=2018]

vets_df = pd.DataFrame(vets, columns=['ID', 'Name', 'Active', 'RookieYear', 'LastSeasonPlayed'])
vets_df = vets_df.drop(columns=['Active', 'RookieYear', 'LastSeasonPlayed'])

kp_id = find_player_id('Porzingis, Kristaps')
shots_json = get_shot_data(kp_id)

shot_data = shots_json['resultSets'][0]['rowSet']
columns = shots_json['resultSets'][0]['headers']

columns_to_drop = ['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'GAME_DATE', 'HTM', 'VTM']

df = pd.DataFrame.from_records(shot_data, columns=columns)
df = df.drop(columns=columns_to_drop)

missed_shot_trace = go.Scatter(
    x = -df[df['EVENT_TYPE'] == 'Missed Shot']['LOC_X'],
    y = df[df['EVENT_TYPE'] == 'Missed Shot']['LOC_Y'],
    mode = 'markers',
    name = 'Miss',
    marker={'color':'blue', 'size':5}
)
made_shot_trace = go.Scatter(
    x = -df[df['EVENT_TYPE'] == 'Made Shot']['LOC_X'],
    y = df[df['EVENT_TYPE'] == 'Made Shot']['LOC_Y'],
    mode = 'markers',
    name='Make',
    marker={'color':'red', 'size':5}
)

data = [missed_shot_trace, made_shot_trace]
layout = go.Layout(
    title='Kristaps Porzingis Shot Chart 2017-2018',
    showlegend =True,
    xaxis={'showgrid':False, 'range':[-300,300]},
    yaxis={'showgrid':False, 'range':[-100,500]},
    height = 600,
    width = 650,
    shapes=court_shapes)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename ='Kristaps Porzingis Shot Chart')
