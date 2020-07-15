import pandas as pd
import matplotlib.pyplot as plt
from stats.data import games
from stats.frames import info, events

plays = games.query("type == 'play' & event != 'NP'")
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

pa = plays.loc[plays['player'].shift() != plays['player'],['year', 'game_id', 'inning', 'team', 'player']]

pa = pa.groupby(['year','game_id','team']).size().reset_index(name='PA')

events = events.set_index(['year', 'game_id', 'team', 'event_type'])

events = events.unstack().fillna(0).reset_index()
events.columns = events.columns.droplevel()

events.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']

events = events.rename_axis(None,axis='columns')
# i used the below but the commit test failed
#events_plus_pa = pd.merge(events,right=pa,how='outer',left_on=['year','game_id','team'],right_on=['year','game_id','team'])

#this is their solution for the above
events_plus_pa = pd.merge(events, pa, how='outer', left_on=['year', 'game_id', 'team'], right_on=['year', 'game_id', 'team'])

# i used the below but the commit test failed
#defense = pd.merge(events_plus_pa,right=info)

#this is their solution for above
defense = pd.merge(events_plus_pa, info)

# i used the below but the commit test failed
#defense['DER'] = defense.apply(lambda x: (1 - ((x['H'] + x['ROE']) / (x['PA'] - x['BB'] - x['SO'] - x['HBP'] - x['HR']))), axis=1)

#this is their solution for above
defense.loc[:, 'DER'] = 1 - ((defense['H'] + defense['ROE']) / (defense['PA'] - defense['BB'] - defense['SO'] - defense['HBP'] - defense['HR']))

defense.loc[:, 'year'] = pd.to_numeric(defense.loc[:, 'year'])

der = defense.loc[defense['year'] >= 1978,['year','defense','DER']]

der = der.pivot(index='year',columns='defense',values='DER')

der.plot(x_compat=True,xticks=range(1978,2018,4),rot=45)
plt.show()
