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

day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211105_15_24_05_analogData.csv")
day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211108_18_59_02_analogData.csv")
day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211109_15_06_40_analogData.csv")
day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211110_14_11_53_analogData.csv")
day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211115_15_54_10_analogData.csv")

touch_sensor_1 = day_1_data['Dev4_ai4'].tolist()
touch_sensor_2 = day_2_data['Dev4_ai4'].tolist()
touch_sensor_3 = day_3_data['Dev4_ai4'].tolist()
touch_sensor_4 = day_4_data['Dev4_ai4'].tolist()
touch_sensor_5 = day_5_data['Dev4_ai4'].tolist()

touch_sensor = touch_sensor_1 + touch_sensor_2 + touch_sensor_3 + touch_sensor_4 + touch_sensor_5

water_1 = day_1_data['Dev4_ai7'].tolist()
water_2 = day_2_data['Dev4_ai7'].tolist()
water_3 = day_3_data['Dev4_ai7'].tolist()
water_4 = day_4_data['Dev4_ai7'].tolist()
water_5 = day_5_data['Dev4_ai7'].tolist()

water = water_1 + water_2 + water_3 + water_4 + water_5

cs_plus_yellow_1 = day_1_data['Dev4_ai14'].tolist()
cs_plus_yellow_2 = day_2_data['Dev4_ai14'].tolist()
cs_plus_yellow_3 = day_3_data['Dev4_ai14'].tolist()
cs_plus_yellow_4 = day_4_data['Dev4_ai14'].tolist()
cs_plus_yellow_5 = day_5_data['Dev4_ai14'].tolist()

cs_plus_yellow = cs_plus_yellow_1 + cs_plus_yellow_2 + cs_plus_yellow_3 + cs_plus_yellow_4 + cs_plus_yellow_5

cs_plus_orange_1 = day_1_data['Dev4_ai13'].tolist()
cs_plus_orange_2 = day_2_data['Dev4_ai13'].tolist()
cs_plus_orange_3 = day_3_data['Dev4_ai13'].tolist()
cs_plus_orange_4 = day_4_data['Dev4_ai13'].tolist()
cs_plus_orange_5 = day_5_data['Dev4_ai13'].tolist()

cs_plus_orange  = cs_plus_orange_1 + cs_plus_orange_2 + cs_plus_orange_3 + cs_plus_orange_4 + cs_plus_orange_5

cs_minus_brown_1 = day_1_data['Dev4_ai12'].tolist()
cs_minus_brown_2 = day_2_data['Dev4_ai12'].tolist()
cs_minus_brown_3 = day_3_data['Dev4_ai12'].tolist()
cs_minus_brown_4 = day_4_data['Dev4_ai12'].tolist()
cs_minus_brown_5 = day_5_data['Dev4_ai12'].tolist()

cs_minus_brown = cs_minus_brown_1 + cs_minus_brown_2 + cs_minus_brown_3 + cs_minus_brown_4 + cs_minus_brown_5

cs_minus_green_1 = day_1_data['Dev4_ai11'].tolist()
cs_minus_green_2 = day_2_data['Dev4_ai11'].tolist()
cs_minus_green_3 = day_3_data['Dev4_ai11'].tolist()
cs_minus_green_4 = day_4_data['Dev4_ai11'].tolist()
cs_minus_green_5 = day_5_data['Dev4_ai11'].tolist()

cs_minus_green = cs_minus_green_1 + cs_minus_green_2 + cs_minus_green_3 + cs_minus_green_4 + cs_minus_green_5

number_of_days = 5
day_count = number_of_days*60

water_start = 0

criterion = {}
keys = range(day_count)
value = [""]*day_count
keys = range(day_count)
value = [""]*day_count

criterion = dict(zip(keys,value))
trial = 0
trial_baseline = 0
trial_range = 22000
time_offset = 1000 #<---- change to look at different time periods relative to water (1000 = 1 s prior to delivery)
    
while trial < day_count:
    for i in range (trial_baseline,trial_range):
        if water[i] > 1:
            water_start = i
            continue
    trial_baseline += 22000
    trial_range += 22000
    touch_sensor_start = water_start - time_offset 
    for i in range(touch_sensor_start,touch_sensor_start+time_offset):
        if touch_sensor[i] > 1:
            criterion[trial] = "true"
    trial += 1


trial = 0
trial_baseline = 0
trial_range = 22000

while trial < day_count:
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
criterion_cs_plus = False
criterion_cs_minus = False
for i in range(len(cs_plus_trials)-window+1):
    criterion_trials_cs_plus = (cs_plus_trials[i:i+window].count(1))
    if criterion_trials_cs_plus >= 16:
        criterion_cs_plus = True
for i in range(len(cs_minus_trials)-window+1):
    criterion_trials_cs_minus = (cs_minus_trials[i:i+window].count(1))
    if criterion_trials_cs_minus <= 4:
        criterion_cs_minus = True


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

if criterion_cs_plus == True:
    print("Congratulations! You have reached criterion for CS+!")
else:
    print("Oh no! You have not reached criterion for CS+!")
    
if criterion_cs_minus == True:
    print("Congratulations! You have reached criterion for CS-!")
else:
    print("Oh no! You have not reached criterion for CS-!")
    
    
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