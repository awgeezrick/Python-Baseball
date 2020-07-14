import pandas as pd
import matplotlib.pyplot as plt
from stats.data import games

attendance = games[['year','multi3']].loc[(games['type'] == 'info') & (games['multi2'] == 'attendance')]

attendance = attendance.rename(columns={'multi3':'Attendance','year':'Year'})

attendance.loc[:,'Attendance'] = pd.to_numeric(attendance.loc[:,'Attendance'])

attendance.plot(x='Year', y='Attendance', figsize=(15, 7),kind='bar')
plt.xlabel(xlabel='Year')
plt.ylabel(ylabel='Attendance')
#plt.axhline(attendance['attendance'].mean(),label='mean',linestyle='dashed',color='green')
plt.axhline(y=attendance['Attendance'].mean(), label='Mean', linestyle='--', color='green')
plt.show()
