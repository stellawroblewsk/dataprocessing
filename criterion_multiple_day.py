# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:23:13 2021

@author: Stella
"""
from pandas import *
import pandas as pd  
import csv
from itertools import zip_longest
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
# from tkinter import Tk, filedialog

# root = Tk() # pointing root to Tk() to use it as Tk() in program.
# root.withdraw() # Hides small tkinter window.
# root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
# open_file = filedialog.askopenfilenames() # returns a tuple with opened file's complete path
# open_file = str(open_file)


# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211121_14_59_43_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211122_11_13_17_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211123_12_30_50_analogData.csv")

day_1_data = pd.read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Analog Data/20211129_13_56_12_analogData.csv")
print('Finito 1')
day_2_data = pd.read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Analog Data/20211130_13_58_21_analogData.csv")
print('Finito 2')
day_3_data = pd.read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Analog Data/20211201_14_22_15_analogData.csv")
print('Finito 3')
day_4_data = pd.read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Analog Data/20211202_16_08_07_analogData.csv")
print('Finito 4')
day_5_data = pd.read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Analog Data/20211203_13_49_09_analogData.csv")
print('Finito 5')
day_6_data = pd.read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Analog Data/20211204_13_57_16_analogData.csv")
print('Finito 6')

touch_sensor_1 = day_1_data['Dev4_ai4'].tolist()
touch_sensor_2 = day_2_data['Dev4_ai4'].tolist()
touch_sensor_3 = day_3_data['Dev4_ai4'].tolist()
touch_sensor_4 = day_4_data['Dev4_ai4'].tolist()
touch_sensor_5 = day_5_data['Dev4_ai4'].tolist()
touch_sensor_6 = day_6_data['Dev4_ai4'].tolist()

touch_sensor = touch_sensor_1 + touch_sensor_2 + touch_sensor_3 + touch_sensor_4 + touch_sensor_5 + touch_sensor_6

water_1 = day_1_data['Dev4_ai7'].tolist()
water_2 = day_2_data['Dev4_ai7'].tolist()
water_3 = day_3_data['Dev4_ai7'].tolist()
water_4 = day_4_data['Dev4_ai7'].tolist()
water_5 = day_5_data['Dev4_ai7'].tolist()
water_6 = day_6_data['Dev4_ai7'].tolist()

water = water_1 + water_2 + water_3 + water_4 + water_5 + water_6

analog_output_1 = day_1_data['Dev4_ai5'].tolist()
analog_output_2 = day_2_data['Dev4_ai5'].tolist()
analog_output_3 = day_3_data['Dev4_ai5'].tolist()
analog_output_4 = day_4_data['Dev4_ai5'].tolist()
analog_output_5 = day_5_data['Dev4_ai5'].tolist()
analog_output_6 = day_6_data['Dev4_ai5'].tolist()

analog_output = analog_output_1 + analog_output_2 + analog_output_3 + analog_output_4 + analog_output_5 + analog_output_6


cs_plus_yellow_1 = day_1_data['Dev4_ai14'].tolist()
cs_plus_yellow_2 = day_2_data['Dev4_ai14'].tolist()
cs_plus_yellow_3 = day_3_data['Dev4_ai14'].tolist()
cs_plus_yellow_4 = day_4_data['Dev4_ai14'].tolist()
cs_plus_yellow_5 = day_5_data['Dev4_ai14'].tolist()
cs_plus_yellow_6 = day_6_data['Dev4_ai14'].tolist()

cs_plus_yellow = cs_plus_yellow_1 + cs_plus_yellow_2 + cs_plus_yellow_3 + cs_plus_yellow_4 + cs_plus_yellow_5 + cs_plus_yellow_6

cs_plus_orange_1 = day_1_data['Dev4_ai13'].tolist()
cs_plus_orange_2 = day_2_data['Dev4_ai13'].tolist()
cs_plus_orange_3 = day_3_data['Dev4_ai13'].tolist()
cs_plus_orange_4 = day_4_data['Dev4_ai13'].tolist()
cs_plus_orange_5 = day_5_data['Dev4_ai13'].tolist()
cs_plus_orange_6 = day_6_data['Dev4_ai13'].tolist()

cs_plus_orange  = cs_plus_orange_1 + cs_plus_orange_2 + cs_plus_orange_3 + cs_plus_orange_4 + cs_plus_orange_5 + cs_plus_orange_6

cs_minus_brown_1 = day_1_data['Dev4_ai12'].tolist()
cs_minus_brown_2 = day_2_data['Dev4_ai12'].tolist()
cs_minus_brown_3 = day_3_data['Dev4_ai12'].tolist()
cs_minus_brown_4 = day_4_data['Dev4_ai12'].tolist()
cs_minus_brown_5 = day_5_data['Dev4_ai12'].tolist()
cs_minus_brown_6 = day_6_data['Dev4_ai12'].tolist()

cs_minus_brown = cs_minus_brown_1 + cs_minus_brown_2 + cs_minus_brown_3 + cs_minus_brown_4 + cs_minus_brown_5 + cs_minus_brown_6

cs_minus_green_1 = day_1_data['Dev4_ai11'].tolist()
cs_minus_green_2 = day_2_data['Dev4_ai11'].tolist()
cs_minus_green_3 = day_3_data['Dev4_ai11'].tolist()
cs_minus_green_4 = day_4_data['Dev4_ai11'].tolist()
cs_minus_green_5 = day_5_data['Dev4_ai11'].tolist()
cs_minus_green_6 = day_6_data['Dev4_ai11'].tolist()

cs_minus_green = cs_minus_green_1+ cs_minus_green_2 + cs_minus_green_3 + cs_minus_green_4 + cs_minus_green_5 + cs_minus_green_6

number_of_days = 6
day_count = number_of_days*60

water_start = 0

criterion = {}
keys = range(day_count)
value = [""]*day_count 

criterion = dict(zip(keys,value))
trial = 0
trial_baseline = 0
trial_range = 22000
criterion_time_range = 1000 #can be changed based on how many seconds prior to water delivery
percentages_cs_p_1 = []
percentages_cs_p_2 = []
percentages_cs_m_1 = []
percentages_cs_m_2 = []
    
while trial < day_count:
    for i in range (trial_baseline,trial_range):
        if analog_output[i] > 4.1:
            #print("yes",trial)
            trial_start = i
            break
    trial_baseline += 22000
    trial_range += 22000
    touch_sensor_start = water_start - criterion_time_range 
    for i in range(trial_start + 11000, trial_start + 12000):
        if touch_sensor[i] > 4:
            criterion[trial] = "true"
    trial += 1


trial = 0
trial_baseline = 0
trial_range = 22000

while trial < day_count :
    for i in range (trial_baseline,trial_range):
        if (cs_plus_yellow[i] > 1):
            trial_type = "cs+1"
        if (cs_plus_orange[i] > 1):
            trial_type = "cs+2"
        if (cs_minus_brown[i] > 1):
            trial_type = "cs-1"
        if (cs_minus_green[i] > 1):
            trial_type = "cs-2"
    trial_baseline += 22000
    trial_range += 22000
    value = criterion[trial] + trial_type
    criterion[trial] = value
    trial += 1
    trial_type = ""


cs_plus_1_trials = []
cs_plus_2_trials = []
cs_minus_1_trials = []
cs_minus_2_trials = []

for i in criterion:
    if ("cs+1" in criterion[i]):
        if 'true' in criterion[i]:
            cs_plus_1_trials.append(1)
        else:
            cs_plus_1_trials.append(0)
    if ("cs+2" in criterion[i]):
        if 'true' in criterion[i]:
            cs_plus_2_trials.append(1)
        else:
            cs_plus_2_trials.append(0)
    if ("cs-1" in criterion[i]):
        if 'true' in criterion[i]:
            cs_minus_1_trials.append(1)
        else:
            cs_minus_1_trials.append(0)
    if ("cs-2" in criterion[i]):
        if 'true' in criterion[i]:
            cs_minus_2_trials.append(1)
        else:
            cs_minus_2_trials.append(0)


window = 20
criterion_cs_plus_1_max = 0
criterion_cs_plus_2_max = 0
criterion_cs_minus_1_min = 20
criterion_cs_minus_2_min = 20
criterion_cs_plus_1 = False
criterion_cs_plus_2 = False
criterion_cs_minus_1 = False
criterion_cs_minus_2 = False

for i in range(len(cs_plus_1_trials)-window+1):
    criterion_trials_cs_plus_1 = (cs_plus_1_trials[i:i+window].count(1))
    if criterion_trials_cs_plus_1 > criterion_cs_plus_1_max:
        criterion_cs_plus_1_max = criterion_trials_cs_plus_1
    if criterion_trials_cs_plus_1 >= 16:
        criterion_cs_plus_1 = True
    percentages_cs_p_1.append(((criterion_trials_cs_plus_1 / 20)*100))

for i in range(len(cs_plus_2_trials)-window+1):
    criterion_trials_cs_plus_2 = (cs_plus_2_trials[i:i+window].count(1))
    if criterion_trials_cs_plus_2 > criterion_cs_plus_2_max:
        criterion_cs_plus_2_max = criterion_trials_cs_plus_2
    if criterion_trials_cs_plus_2 >= 16:
        criterion_cs_plus_2 = True
    percentages_cs_p_2.append(((criterion_trials_cs_plus_2 / 20)*100))
    
for i in range(len(cs_minus_1_trials)-window+1):
    criterion_trials_cs_minus_1 = (cs_minus_1_trials[i:i+window].count(1))
    if criterion_trials_cs_minus_1 <= 4:
        criterion_cs_minus_1 = True
    if criterion_trials_cs_minus_1 < criterion_cs_minus_1_min: 
        criterion_cs_minus_1_min = criterion_trials_cs_minus_1
    percentages_cs_m_1.append(((criterion_trials_cs_minus_1 / 20)*100))

for i in range(len(cs_minus_2_trials)-window+1):
    criterion_trials_cs_minus_2 = (cs_minus_2_trials[i:i+window].count(1))
    if criterion_trials_cs_minus_2 <= 4:
        criterion_cs_minus_2 = True
    if criterion_trials_cs_minus_2 < criterion_cs_minus_2_min: 
        criterion_cs_minus_2_min = criterion_trials_cs_minus_2
    percentages_cs_m_2.append(((criterion_trials_cs_minus_2 / 20)*100))


#print(criterion)

if criterion_cs_plus_1 == True:
    print("Congratulations! You have reached criterion for CS+1!")
else:
    print("Oh no! You have not reached criterion for CS+1!")
    print("Your maximum value of correctly licking to CS+1 was ", str(criterion_cs_plus_1_max), " out of 20 consecutive trials")

if criterion_cs_plus_2 == True:
    print("Congratulations! You have reached criterion for CS+2!")
else:
    print("Oh no! You have not reached criterion for CS+2!")
    print("Your maximum value of correctly licking to CS+2 was ", str(criterion_cs_plus_2_max), " out of 20 consecutive trials")
    
if criterion_cs_minus_1 == True:
    print("Congratulations! You have reached criterion for CS-1!")
else:
    print("Oh no! You have not reached criterion for CS-1!")
    print("Your minimum value of correctly not licking to CS-1 was ", str(criterion_cs_minus_1_min), " out of 20 consecutive trials")

if criterion_cs_minus_2 == True:
    print("Congratulations! You have reached criterion for CS-2!")
else:
    print("Oh no! You have not reached criterion for CS-2!")
    print("Your minimum value of correctly not licking to CS-2 was ", str(criterion_cs_minus_2_min), " out of 20 consecutive trials")
    
    
#general lick count over all trials
cs_plus_1_licked_total = 0
cs_plus_2_licked_total = 0
cs_minus_1_licked_total = 0
cs_minus_2_licked_total = 0
cs_plus_1_none_total = 0
cs_plus_2_none_total = 0
cs_minus_1_none_total = 0
cs_minus_2_none_total = 0

for i in criterion:
    if ("cs+1" in criterion[i]):
        if 'true' in criterion[i]:
            cs_plus_1_licked_total +=1 
        else:
            cs_plus_1_none_total +=1
    if ("cs+2" in criterion[i]):
        if 'true' in criterion[i]:
            cs_plus_2_licked_total +=1 
        else:
            cs_plus_2_none_total +=1    
    if ("cs-1" in criterion[i]):
        if 'true' in criterion[i]:
            cs_minus_1_licked_total += 1
        else:
            cs_minus_1_none_total += 1
    if ("cs-2" in criterion[i]):
        if 'true' in criterion[i]:
            cs_minus_2_licked_total += 1
        else:
            cs_minus_2_none_total += 1

cs_plus_1_percent = (cs_plus_1_licked_total/(cs_plus_1_licked_total + cs_plus_1_none_total))*100
cs_plus_2_percent = (cs_plus_2_licked_total/(cs_plus_2_licked_total + cs_plus_2_none_total))*100
cs_minus_1_percent = (cs_minus_1_licked_total/(cs_minus_1_licked_total + cs_minus_1_none_total))*100
cs_minus_2_percent = (cs_minus_2_licked_total/(cs_minus_2_licked_total + cs_minus_2_none_total))*100

print("In all CS+1 trials this mouse licked in", cs_plus_1_percent, "% of trials")
print("In all CS+2 trials this mouse licked in", cs_plus_2_percent, "% of trials")
print("In all CS-1 trials this mouse licked in", cs_minus_1_percent, "% of trials")
print("In all CS-2 trials this mouse licked in", cs_minus_2_percent, "% of trials")

df1 = pd.DataFrame({'CS+1': percentages_cs_p_1})
df2 = pd.DataFrame({'CS+2': percentages_cs_p_2})
df3 = pd.DataFrame({'CS-1': percentages_cs_m_1})
df4 = pd.DataFrame({'CS-2': percentages_cs_m_2})

pd.concat([df1,df2,df3,df4],axis=1).to_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Processed Data/12-3-criterion-percentages-mouse5-5days.csv', index=False)

print("cs+ percentages:", percentages_cs_p_1)
print("cs+ percentages:", percentages_cs_p_2)
print("cs-1 percentages:", percentages_cs_m_1)   
print("cs-2 percentages:", percentages_cs_m_2)
