import pandas as pd
import matplotlib.pyplot as plt
from stats.data import games

attendance = games[['year','multi3']].loc[(games['type'] == 'info') & (games['multi2'] == 'attendance')]

attendance = attendance.rename(columns={'multi3':'attendance'})

attendance.loc[:,'attendance'] = pd.to_numeric(attendance.loc[:,'attendance'])

attendance.plot(x='year', y='attendance', figsize=(15, 7),kind='bar')
plt.xlabel(xlabel='year')
plt.ylabel(ylabel='attendance')
plt.axhline(attendance['attendance'].mean(),label='mean',linestyle='dashed',color='green')
plt.show()
