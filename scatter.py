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


####Below, adjust any analog input port 

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

analog_output_1 = day_1_data['Dev4_ai5'].tolist()
analog_output_2 = day_2_data['Dev4_ai5'].tolist()
analog_output_3 = day_3_data['Dev4_ai5'].tolist()
analog_output_4 = day_4_data['Dev4_ai5'].tolist()
analog_output_5 = day_5_data['Dev4_ai5'].tolist()
analog_output_6 = day_6_data['Dev4_ai5'].tolist()

analog_output = analog_output_1 + analog_output_2 + analog_output_3 + analog_output_4 + analog_output_5 + analog_output_6

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


water_start = 0

number_of_days = 6
day_count = number_of_days*60

trials = 60 * number_of_days
trial_start = 0

criterion = {}


trial = 0
trial_baseline = 0
trial_range = 22000
time_from_beginning = 11000 #<---- change based on how long from the beginning of the trial you want to start recording (1000 = 1 s after start of the trial)
stop_reading = 1000 #<------ change based on how long you want to read


yellow_licks =[0]*trials
yellow_trials = 0
yellow_index = -1 

orange_licks =[0]*trials
orange_trials = 0
orange_index = -1

brown_licks = [0]*trials
brown_trials = 0
brown_index = -1

green_licks = [0]*trials
green_trials = 0
green_index = -1



#fliter_by_trial_type = True  #<---------- change to True if you want to output csv files separated by trials with data for all other analog inputs 



while trial < trials:
    
    curr_trial = ""
    for i in range (trial_baseline,trial_range):
        if analog_output[i] > 4.1:
            #print("yes",trial)
            trial_start = i
            break
    
    curr_trial_type = ""
    
    for i in range(trial_start, trial_start + 7000):

        if (analog_output[i] > 1.8 and analog_output[i]<2.2):
            curr_trial_type = "yellow"
            yellow_index += 1
            break
        elif (analog_output[i] > 2.3 and analog_output[i]<2.7):
            orange_index += 1
            curr_trial_type = "orange"
            break
        elif (analog_output[i] > 2.8 and analog_output[i]<3.2):
            green_index += 1
            curr_trial_type = "green"
            break
        elif (analog_output[i] > 3.3 and analog_output[i]<3.7):
            brown_index += 1
            curr_trial_type = "brown"
            break
    
    touch_sensor_start =  trial_start + time_from_beginning
    touch_sensor_end = touch_sensor_start + stop_reading
    is_lick = False


    
    for j in range (touch_sensor_start, touch_sensor_end): 
        
        if (touch_sensor[j] > 1) and (is_lick == False):
            if curr_trial_type == "yellow":
                # yellow_trials += 1
                yellow_licks[yellow_index] += 1
                is_lick = True
            elif curr_trial_type == "orange":
                # orange_trials += 1
                orange_licks[orange_index] += 1
                is_lick = True
            elif curr_trial_type == "brown":
                #brown_trials +=1
                brown_licks[brown_index] += 1
                is_lick = True
            elif curr_trial_type == "green":
                # green_trials += 1
                green_licks[green_index] += 1
                is_lick = True
                
        elif touch_sensor[j] < 1:
            is_lick = False
        
    trial_baseline += 22000
    trial_range += 22000
    trial += 1
    print(trial)

yellow_licks = [i for i in yellow_licks if i != 0]
orange_licks =  [i for i in orange_licks if i != 0]
brown_licks =  [i for i in brown_licks if i != 0]
green_licks =  [i for i in green_licks if i != 0]

df1 = pd.DataFrame({'CS+1':yellow_licks})
df2 = pd.DataFrame({'CS+2':orange_licks})
df3 = pd.DataFrame({'CS-1':brown_licks})
df4 = pd.DataFrame({'CS-2':green_licks})
pd.concat([df1,df2,df3,df4],axis=1).to_csv('11-19-1108-bigfile.csv', index=False)












































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


