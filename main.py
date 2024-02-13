import pandas as pd
import numpy

#Import Players, Teams, Stats from NBA API
from nba_api.stats.static import players
from nba_api.stats.static import teams
player_dict = players.get_players()
team_dict = teams.get_teams()
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import commonplayerinfo
active_players = players.get_active_players()


dame = [player for player in player_dict if player['full_name'] == 'Damian Lillard'][0]
print(dame)
gamelog_dame = playergamelog.PlayerGameLog(player_id=203081, season = '2023')
gamelog_dame_df = gamelog_dame.get_data_frames()[0]
print(gamelog_dame_df)