import os
import glob
import pandas as pd

# create a list of the location of all the game files that end in 'eve' from the games directory
game_files = glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))

list.sort(game_files)

#game_frames list to hold the generated dataframes from the for in loop below
game_frames = []

for game_file in game_files:
    game_frame = pd.read_csv(game_file,names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# this concats all the dataframes in the game_frames list into one dataframe
games = pd.concat(game_frames, ignore_index=True)

games['multi5'] = games['multi5'].replace('??','')

identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

identifiers.fillna(method='ffill',inplace=True)
identifiers.rename(columns={0:'game_id',1:'year'},inplace=True)

games = pd.concat([games,identifiers],axis=1,sort=False)

games.fillna('',inplace=True)

games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

print(games.head())
