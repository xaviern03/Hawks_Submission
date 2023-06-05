import pandas as pd


def divider():
    print('----------------------', end='\n')

draft_file = input('Enter route to draft data file in format C:/Users/Username/etc. : \n')

divider()

# Variable assigned to read from NBA draft data.       
draft = pd.read_csv(draft_file)  

# Dictionary that will hold the values for Duke players drafted in or before 2000.
duke_count = {}

# Dictionary that will hold the values for letters. 
letter_count = {}

# Adds the team to letter_count dictionary if not already there. If team is already in the dictionary then adds plus 1 to the value.
for i in range(len(draft)):
    if (draft.loc[i, 'player'][0] == 'D') and (((draft.loc[i, 'year'])%2) == 0):
        if draft.loc[i, 'team'] in letter_count:
            letter_count[draft.loc[i,'team']] += 1
        else:
            letter_count[draft.loc[i, 'team']] = 1

# Adds the team to the duke_count dictionary if not already there. If the team is already in the dictionary then adds plus 1 to the value.
for i in range(len(draft)):
    if (draft.loc[i,'college'] == 'Duke') and (draft.loc[i, 'year'] <= 2000):
        if draft.loc[i, 'team'] in duke_count:
            duke_count[draft.loc[i,'team']] += 1
        else:
            duke_count[draft.loc[i,'team']] = 1
    else:
        continue

# Function that finds the max value(s) of a dictinary.
def team_max(team_count):
    team_list = []
    team_max = max(team_count.values())
    for team in team_count:
        if team_count[team] == team_max:
            team_list.append(team + ':' + str(team_max))
    return team_list



print('The NBA teams with the most Duke players drafted in or before the 2000 draft are: \n', team_max(duke_count))
divider()
print("The NBA teams that drafted the most players who's first name start with the letter D in an even year draft are: \n", team_max(letter_count))


'''
References:

https://stackoverflow.com/questions/18039057/python-pandas-error-tokenizing-data

https://www.w3schools.com/python/pandas/pandas_dataframes.asp

'''

    
 




