import pandas as pd
import matplotlib.pyplot as plt


def divider():
    print(" ")
    print("-----------------------------")
    print(" ")

print("Part a. \n")

draft_file = input('Enter route to draft data file in format C:/Users/Username/etc. : \n')

draft = pd.read_csv(draft_file)

draft_slot = input("What draft pick would you like to value? \n")
pick_dict = {}

# Function that finds the average of the box_plus_minus value at a certain pick then adds it to a dictionary.
def pick_average(data,pick,dict):
    pick_list = []
    for i in range(len(draft)):
        if pick == draft.loc[i, 'overall_pick']:
            pick_list.append(draft.loc[i,'box_plus_minus'])
    clean_list = [num for num in pick_list if num == num]
    pick_avg = round(sum(clean_list) / len(clean_list),1)
    if pick in dict:
        return dict
    else:
        dict["Pick - " + str(pick)] = str(pick_avg)

# Executing the function in a loop to add them to pick_dict.
for i in range(60):
    pick_average(draft,i+1,pick_dict)

# Setting the x and y values to then add them to a scatter plot.
pick_x = []
for i in range(1,61):
    pick_x.append(i)

pick_y = [] 
for i in range(1,61):
    pick_y.append(pick_dict['Pick - ' + str(i)])

plt.scatter(pick_x,pick_y)
plt.title("NBA Draft Slot Value")
plt.xlabel("Draft Slot")
plt.ylabel("Average Player Performance of Draft Slot")
plt.show()

# Function that returns the draft value of each pick based on a basic grading system.
def draft_value(pick,pick_dict):
    if float(pick_dict['Pick - ' + str(pick)]) >= -0.75:
        return 'On average draft pick ' + pick + ' is an excellent pick slot.'
    elif float(pick_dict['Pick - ' + str(pick)]) >= -3 and float(pick_dict['Pick - ' + str(pick)]) < -0.75:
        return 'On average draft pick ' + pick + ' is a good pick slot.'
    elif float(pick_dict['Pick - ' + str(pick)]) >= -5.25 and float(pick_dict['Pick - ' + str(pick)]) < -3:
        return 'On average draft pick ' + pick + ' is an ok pick slot.'
    elif float(pick_dict['Pick - ' + str(pick)]) < -5.25:
        return 'On average draft pick ' + pick + ' is a poor pick slot.'

print(draft_value(draft_slot,pick_dict))


divider()
print("Part b. \n")

over_dict = {}
under_dict = {}

# Loop that adds key value pairs to over/under_dict if not already there. If key is already present in the dict adds + 1 to the value.
for i in range(len(draft)):
    if float(draft.loc[i,'box_plus_minus']) > float(pick_dict['Pick - ' + str(draft.loc[i,'overall_pick'])]):
        if draft.loc[i,'team'] in over_dict:
            over_dict[draft.loc[i,'team']] += 1
        else:
            over_dict[draft.loc[i,'team']] = 1
    elif float(draft.loc[i, 'box_plus_minus']) < float(pick_dict['Pick - ' + str(draft.loc[i,'overall_pick'])]):
        if draft.loc[i,'team'] in under_dict:
            under_dict[draft.loc[i,'team']] += 1
        else:
            under_dict[draft.loc[i,'team']] = 1

# Finds the max values for the over and under dictionaries and adds them to a list.
max_over = max(over_dict.values())
max_over_team = [team for team, value in over_dict.items() if value == max_over]

max_under = max(under_dict.values())
max_under_team = [team for team, value in under_dict.items() if value == max_under]

# Adds the over and under key and value pairs to seperate lists.
team_key = list(over_dict.keys())
team_over = list(over_dict.values())
team_under = list(under_dict.values())

# Creates a bar graph for the over key, value pairs.
plt.bar(team_key, team_over, color='blue', width=0.5)
plt.title("NBA Teams that Overperformed in the Draft")
plt.xlabel("NBA Teams")
plt.ylabel("Number of Overperforming Draft Picks")
plt.xticks(rotation='vertical')
plt.show()

#Creates a bar graph for the under key, value pairs.
plt.bar(team_key, team_under, color='red', width=0.5)
plt.title("NBA Teams that Underperformed in the Draft")
plt.xlabel("NBA Teams")
plt.ylabel("Number of Underperforming Draft Picks")
plt.xticks(rotation='vertical')
plt.show()


divider()
print("The teams that have over performed the most in the NBA Draft are " + ' and '.join(max_over_team) + '.')

divider()
print("The teams that have under performed the most in the NBA Draft are " + ' and '.join(max_under_team) + '.')

college_dict = {}

# Loop that adds key value pairs to over/under_dict if not already there. If key is already present in the dict adds + 1 to the value.
for i in range(len(draft)):
   if pd.isna(draft.loc[i,'college']):
    continue
   else:
    if float(draft.loc[i,'box_plus_minus']) > float(pick_dict['Pick - ' + str(draft.loc[i,'overall_pick'])]):
        if draft.loc[i,'college'] in college_dict:
            college_dict[draft.loc[i,'college']] += 1
        else:
            college_dict[draft.loc[i,'college']] = 1

# Finds max values for college_dict and puts them in a list.
max_college_val = max(college_dict.values())
max_college = [college for college, value in college_dict.items() if value == max_college_val]

# Sorts the college values in the list
college_sort = sorted(college_dict.items(), key=lambda x: x[1], reverse=True)

# Slices the list so that it only shows the top 10 values.
n=10
top_colleges = college_sort[:n]

college_key = [college[0] for college in top_colleges]
college_over = [college[1] for college in top_colleges]


# Creates a bar graph with the top 10 values
plt.bar(college_key, college_over, color='blue', width=0.5)
plt.title("College Teams Whose Players Exceeded Expectation")
plt.xlabel("Colleges")
plt.ylabel("Number of Overperforming Players")
plt.xticks(rotation='vertical')
plt.show()


divider()
print("The college team that has had the most players outperform expectations after entering the NBA is " + ''.join(max_college) + '.')

'''
References:

https://dzone.com/articles/types-of-matplotlib-in-python#:~:text=Matplotlib%20in%20Python%20is%20a,plot%20for%20viewing%20the%20data.

https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda#:~:text=To%20define%20lambda%2C%20you%20specify,as%20the%20third%20argument(Optional.

https://www.w3schools.com/python/ref_func_sorted.asp
'''




