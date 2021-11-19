# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:23:13 2021

@author: Stella
"""
from pandas import *
import pandas as pd  
import csv
from itertools import zip_longest


#MOUSE 9 (HALO)
day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211108_13_09_30_analogData.csv")
day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211109_12_28_09_analogData.csv")
day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211110_11_12_07_analogData.csv")
day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211111_12_07_46_analogData.csv")
day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211115_17_47_48_analogData.csv")
day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211116_15_40_09_analogData.csv")

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

cs_minus_green = cs_minus_green_1 + cs_minus_green_2 + cs_minus_green_3 + cs_minus_green_4 + cs_minus_green_5 + cs_minus_green_6

number_of_days = 6
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
    for i in range(water_start, water_start + 50): #to get collection data change range to (water start, 50) (.025 is the water collection time+0.025 extra)
        if touch_sensor[i] > 1:
            criterion[trial] = "true"
    trial += 1


trial = 0
trial_baseline = 0
trial_range = 22000

while trial < day_count:
    for i in range (trial_baseline,trial_range):
        if (cs_plus_yellow[i] > 1):
            trial_type = "yellow_cs+"
        elif (cs_plus_orange[i] > 1):
            trial_type = "orange_cs+"
        elif cs_minus_brown[i] > 1:
            trial_type = "brown_cs-"
        elif cs_minus_green[i] > 1:
            trial_type = "green_cs-"
        
    trial_baseline += 22000
    trial_range += 22000
    value = criterion[trial] + trial_type
    criterion[trial] = value
    trial += 1
    trial_type = ""


cs_plus_trials_yellow = []
cs_plus_trials_orange = []
cs_minus_trials_brown = []
cs_minus_trials_green = []
for i in criterion:
    if ("yellow" in criterion[i]):
        if 'true' in criterion[i]:
            cs_plus_trials_yellow.append(1)
        else:
            cs_plus_trials_yellow.append(0)
    elif ("orange" in criterion[i]):
        if 'true' in criterion[i]:
            cs_plus_trials_orange.append(1)
        else:
            cs_plus_trials_orange.append(0)
    elif ("brown" in criterion[i]):
        if 'true' in criterion[i]:
            cs_minus_trials_brown.append(1)
        else:
            cs_minus_trials_brown.append(0)
    elif ("green" in criterion[i]):
        if 'true' in criterion[i]:
            cs_minus_trials_green.append(1)
        else:
            cs_minus_trials_green.append(0)



# df1 = ({'cs_plus_trials_yellow': cs_plus_trials_yellow})
# df2 = ({'cs_plus_trials_orange': cs_plus_trials_orange})
# df3 = ({'cs_minus_trials_brown': cs_minus_trials_brown})
# df4 = ({ 'cs_minus_trials_green': cs_minus_trials_green})
       
# pd.concat([df1,df2,df3,df4],axis=1).to_csv('Mouse_3_CONSM.csv', index = False)

d = [cs_plus_trials_yellow,cs_plus_trials_orange,cs_minus_trials_brown,cs_minus_trials_green]

with open("Mouse_9_CONSM.csv","w+") as f:
    writer = csv.writer(f)
    for values in zip_longest(*d):
        writer.writerow(values)

# window = 20
# criterion_cs_plus_yellow = False
# criterion_cs_minus_brown = False
# criterion_cs_plus_orange = False
# criterion_cs_minus_green = False
# for i in range(len(cs_plus_trials_yellow)-window+1):
#     criterion_trials_cs_plus_yellow = (cs_plus_trials_yellow[i:i+window].count(1))
#     if criterion_trials_cs_plus_yellow >= 16:
#         criterion_cs_plus_yellow = True
# for i in range(len(cs_minus_trials_brown)-window+1):
#     criterion_trials_cs_minus_brown = (cs_minus_trials_brown[i:i+window].count(1))
#     if criterion_trials_cs_minus_brown <= 4:
#         criterion_cs_minus_brown = True
# for i in range(len(cs_plus_trials_orange)-window+1):
#     criterion_trials_cs_plus_orange = (cs_plus_trials_orange[i:i+window].count(1))
#     if criterion_trials_cs_plus_orange >= 16:
#         criterion_cs_plus_orange = True
# for i in range(len(cs_minus_trials_green)-window+1):
#     criterion_trials_cs_minus_green = (cs_minus_trials_green[i:i+window].count(1))
#     if criterion_trials_cs_minus_green <= 4:
#         criterion_cs_minus_green = True

# #general lick count over all trials
# cs_plus_licked_total = 0
# cs_minus_licked_total = 0
# cs_plus_none_total = 0
# cs_minus_none_total = 0

# for i in criterion:
#     if ("cs+" in criterion[i]):
#         if 'true' in criterion[i]:
#             cs_plus_licked_total +=1 
#         else:
#             cs_plus_none_total +=1 
#     if ("cs-" in criterion[i]):
#         if 'true' in criterion[i]:
#             cs_minus_licked_total += 1
#         else:
#             cs_minus_none_total += 1

# cs_minus_percent = (cs_minus_licked_total/(cs_minus_licked_total + cs_minus_none_total))*100
# cs_plus_percent = (cs_plus_licked_total/(cs_plus_licked_total + cs_plus_none_total))*100

# print("In all CS+ trials this mouse licked in", cs_plus_percent, "% of trials")
# print("In all CS- trials this mouse licked in", cs_minus_percent, "% of trials")

# if criterion_cs_plus_yellow == True:
#     print("Congratulations! You have reached criterion for CS+ (yellow)!")
# else:
#     print("Oh no! You have not reached criterion for CS+ (yellow)!")

# if criterion_cs_plus_orange == True:
#     print("Congratulations! You have reached criterion for CS+ (orange)!")
# else:
#     print("Oh no! You have not reached criterion for CS+ (orange)!")

# if criterion_cs_minus_brown == True:
#     print("Congratulations! You have reached criterion for CS- (brown)!")
# else:
#     print("Oh no! You have not reached criterion for CS-! (brown)")
    
# if criterion_cs_minus_green == True:
#     print("Congratulations! You have reached criterion for CS- (green)!")
# else:
#     print("Oh no! You have not reached criterion for CS- (green)!")
    
    







#MOUSE 1 (HALO)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 1/20211108_14_00_13_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 1/20211109_13_16_05_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 1/20211110_11_44_51_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 1/20211111_12_34_11_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 1/20211115_18_13_21_analogData.csv")


#MOUSE 2 (HALO)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 2/20211108_14_41_00_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 2/20211109_13_44_21_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 2/20211110_12_15_04_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 2/20211111_16_39_07_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 2/20211115_18_38_49_analogData.csv")


#MOUSE 3 (YFP)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211105_13_26_40_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211108_15_20_52_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211109_14_12_03_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211110_13_05_59_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211115_14_54_04_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/20211116_12_09_27_analogData.csv")


#MOUSE 4 (YFP)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211105_14_35_23_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211108_15_54_14_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211109_14_39_28_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211110_13_40_14_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211115_15_23_52_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211116_12_35_44_analogData.csv")


#MOUSE 5 (HALO)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211105_15_24_05_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211108_18_59_02_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211109_15_06_40_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211110_14_11_53_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211115_15_54_10_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/20211116_13_01_50_analogData.csv")


#MOUSE 6 (HALO)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/20211105_16_23_20_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/20211108_16_46_42_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/20211109_15_35_36_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/20211110_14_40_19_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/20211115_16_24_52_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/20211116_14_20_01_analogData.csv")


#MOUSE 7 (YFP)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/20211105_17_55_41_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/20211108_19_30_52_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/20211109_16_04_21_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/20211110_15_10_43_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/20211115_16_51_00_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/20211116_14_47_05_analogData.csv")


#MOUSE 8 (YFP)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/20211108_12_22_50_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/20211109_11_55_34_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/20211110_10_43_28_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/20211111_11_36_03_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/20211115_17_19_28_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/20211116_15_13_18_analogData.csv")

#MOUSE 9 (HALO)
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211108_13_09_30_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211109_12_28_09_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211110_11_12_07_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211111_12_07_46_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211115_17_47_48_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211116_15_40_09_analogData.csv")


