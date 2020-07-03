import os
import glob
import pandas as pd

# man, my original code kept failing because I was using proper practices like inplace=True, whereas
# the test kept wanting me to redeclare the variable. 


# create a list of the location of all the game files that end in 'eve' from the games directory
game_files = glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))

game_files.sort()

#game_frames list to hold the generated dataframes from the for in loop below
game_frames = []

for game_file in game_files:
    game_frame = pd.read_csv(game_file,names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# this concats all the dataframes in the game_frames list into one dataframe
#games = pd.concat(game_frames, ignore_index=True)
games = pd.concat(game_frames)

games.loc[games['multi5'] == '??', ['multi5']] = ''

identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers = identifiers.fillna(method='ffill')
identifiers.columns = ['game_id', 'year']

games = pd.concat([games,identifiers],axis=1,sort=False)

games = games.fillna(' ')

games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

print(games.head())
