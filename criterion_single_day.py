# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:23:13 2021

@author: Stella
"""
from pandas import *
# from tkinter import Tk, filedialog

# root = Tk() # pointing root to Tk() to use it as Tk() in program.
# root.withdraw() # Hides small tkinter window.
# root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
# open_file = filedialog.askopenfilenames() # returns a tuple with opened file's complete path
# open_file = str(open_file)

data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211116_12_35_44_analogData.csv")

touch_sensor = data['Dev4_ai4'].tolist()

water = data['Dev4_ai7'].tolist()

cs_plus_yellow = data['Dev4_ai14'].tolist()
cs_plus_orange = data['Dev4_ai13'].tolist()

cs_minus_brown = data['Dev4_ai12'].tolist()
cs_minus_green = data['Dev4_ai11'].tolist()

water_start = 0

criterion = {}
keys = range(60)
value = [""]*60
keys = range(60)
value = [""]*60

criterion = dict(zip(keys,value))
trial = 0
trial_baseline = 0
trial_range = 22000
criterion_time_range = 1000 #can be changed based on how many seconds prior to water delivery
    
while trial < 60:
    for i in range (trial_baseline,trial_range):
        if water[i] > 1:
            water_start = i
            continue
    trial_baseline += 22000
    trial_range += 22000
    touch_sensor_start = water_start - criterion_time_range 
    for i in range(touch_sensor_start,touch_sensor_start + criterion_time_range):
        if touch_sensor[i] > 1:
            criterion[trial] = "true"
    trial += 1


trial = 0
trial_baseline = 0
trial_range = 22000

while trial < 60:
    for i in range (trial_baseline,trial_range):
        if (cs_plus_yellow[i] > 1) or (cs_plus_orange[i] > 1):
            trial_type = "cs+"

        if cs_minus_brown[i] > 1 or cs_minus_green[i] > 1:
            trial_type = "cs-"
    trial_baseline += 22000
    trial_range += 22000
    value = criterion[trial] + trial_type
    criterion[trial] = value
    trial += 1
    trial_type = ""


cs_plus_trials = []
cs_minus_trials = []

for i in criterion:
    if ("cs+" in criterion[i]):
        if 'true' in criterion[i]:
            cs_plus_trials.append(1)
        else:
            cs_plus_trials.append(0)
    if ("cs-" in criterion[i]):
        if 'true' in criterion[i]:
            cs_minus_trials.append(1)
        else:
            cs_minus_trials.append(0)


window = 20
criterion_cs_plus_max = 0
criterion_cs_minus_min = 20
criterion_cs_plus = False
criterion_cs_minus = False
for i in range(len(cs_plus_trials)-window+1):
    criterion_trials_cs_plus = (cs_plus_trials[i:i+window].count(1))
    if criterion_trials_cs_plus > criterion_cs_plus_max:
        criterion_cs_plus_max = criterion_trials_cs_plus
    if criterion_trials_cs_plus >= 16:
        criterion_cs_plus = True
for i in range(len(cs_minus_trials)-window+1):
    criterion_trials_cs_minus = (cs_minus_trials[i:i+window].count(1))
    if criterion_trials_cs_minus <= 4:
        criterion_cs_minus = True
    if criterion_trials_cs_minus < criterion_cs_minus_min:
        criterion_cs_minus_min = criterion_trials_cs_minus

#print(criterion)

if criterion_cs_plus == True:
    print("Congratulations! You have reached criterion for CS+!")
else:
    print("Oh no! You have not reached criterion for CS+!")
    print("Your maximum value of correctly licking to CS+ was ", str(criterion_cs_plus_max), " out of 20 consecutive trials")
    
if criterion_cs_minus == True:
    print("Congratulations! You have reached criterion for CS-!")
else:
    print("Oh no! You have not reached criterion for CS-!")
    print("Your minimum value of correctly not licking to CS- was ", str(criterion_cs_minus_min), " out of 20 consecutive trials")
    
    
    
    
    #general lick count over all trials
cs_plus_licked_total = 0
cs_minus_licked_total = 0
cs_plus_none_total = 0
cs_minus_none_total = 0

for i in criterion:
    if ("cs+" in criterion[i]):
        if 'true' in criterion[i]:
            cs_plus_licked_total +=1 
        else:
            cs_plus_none_total +=1 
    if ("cs-" in criterion[i]):
        if 'true' in criterion[i]:
            cs_minus_licked_total += 1
        else:
            cs_minus_none_total += 1

cs_minus_percent = (cs_minus_licked_total/(cs_minus_licked_total + cs_minus_none_total))*100
cs_plus_percent = (cs_plus_licked_total/(cs_plus_licked_total + cs_plus_none_total))*100

print("In all CS+ trials this mouse licked in", cs_plus_percent, "% of trials")
print("In all CS- trials this mouse licked in", cs_minus_percent, "% of trials")