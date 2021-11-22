
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


day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211121_15_28_09_analogData.csv")
day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/20211122_11_38_32_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211110_11_12_07_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211111_12_07_46_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211115_17_47_48_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/20211116_15_40_09_analogData.csv")

time_1 = day_1_data['Time'].tolist()
time_2 = day_2_data['Time'].tolist()
# time_3 = day_3_data['Time'].tolist()
# time_4 = day_4_data['Time'].tolist()
# time_5 = day_5_data['Time'].tolist()
# time_6 = day_6_data['Time'].tolist()

time = time_1 + time_2 #+ time_3 + time_4 + time_5 + time_6


PID_1 = day_1_data['Dev4_ai0'].tolist()
PID_2 = day_2_data['Dev4_ai0'].tolist()
# PID_3 = day_3_data['Dev4_ai0'].tolist()
# PID_4 = day_4_data['Dev4_ai0'].tolist()
# PID_5 = day_5_data['Dev4_ai0'].tolist()
# PID_6 = day_6_data['Dev4_ai0'].tolist()

PID = PID_1 + PID_2 #+ PID_3 + PID_4 + PID_5 + PID_6

motion_sensor_1 = day_1_data['Dev4_ai1'].tolist()
motion_sensor_2 = day_2_data['Dev4_ai1'].tolist()
# motion_sensor_3 = day_3_data['Dev4_ai1'].tolist()
# motion_sensor_4 = day_4_data['Dev4_ai1'].tolist()
# motion_sensor_5 = day_5_data['Dev4_ai1'].tolist()
# motion_sensor_6 = day_6_data['Dev4_ai1'].tolist()

motion_sensor = motion_sensor_1 + motion_sensor_2 #+ motion_sensor_3 + motion_sensor_4 + motion_sensor_5 + motion_sensor_6

camera_trigger_1 = day_1_data['Dev4_ai2'].tolist()
camera_trigger_2 = day_2_data['Dev4_ai2'].tolist()
# camera_trigger_3 = day_3_data['Dev4_ai2'].tolist()
# camera_trigger_4 = day_4_data['Dev4_ai2'].tolist()
# camera_trigger_5 = day_5_data['Dev4_ai2'].tolist()
# camera_trigger_6 = day_6_data['Dev4_ai2'].tolist()

camera_trigger = camera_trigger_1 + camera_trigger_2 #+ camera_trigger_3 + camera_trigger_4 + camera_trigger_5 + camera_trigger_6

laser_1 = day_1_data['Dev4_ai3'].tolist()
laser_2 = day_2_data['Dev4_ai3'].tolist()
# laser_3 = day_3_data['Dev4_ai3'].tolist()
# laser_4 = day_4_data['Dev4_ai3'].tolist()
# laser_5 = day_5_data['Dev4_ai3'].tolist()
# laser_6 = day_6_data['Dev4_ai3'].tolist()

laser = laser_1 + laser_2 #+ laser_3 + laser_4 + laser_5 + laser_6


touch_sensor_1 = day_1_data['Dev4_ai4'].tolist()
touch_sensor_2 = day_2_data['Dev4_ai4'].tolist()
# touch_sensor_3 = day_3_data['Dev4_ai4'].tolist()
# touch_sensor_4 = day_4_data['Dev4_ai4'].tolist()
# touch_sensor_5 = day_5_data['Dev4_ai4'].tolist()
# touch_sensor_6 = day_6_data['Dev4_ai4'].tolist()

touch_sensor = touch_sensor_1 + touch_sensor_2 #+ touch_sensor_3 + touch_sensor_4 + touch_sensor_5 + touch_sensor_6

analog_output_1 = day_1_data['Dev4_ai5'].tolist()
analog_output_2 = day_2_data['Dev4_ai5'].tolist()
# analog_output_3 = day_3_data['Dev4_ai5'].tolist()
# analog_output_4 = day_4_data['Dev4_ai5'].tolist()
# analog_output_5 = day_5_data['Dev4_ai5'].tolist()
# analog_output_6 = day_6_data['Dev4_ai5'].tolist()

analog_output = analog_output_1 + analog_output_2 #+ analog_output_3 + analog_output_4 + analog_output_5 + analog_output_6

water_1 = day_1_data['Dev4_ai7'].tolist()
water_2 = day_2_data['Dev4_ai7'].tolist()
# water_3 = day_3_data['Dev4_ai7'].tolist()
# water_4 = day_4_data['Dev4_ai7'].tolist()
# water_5 = day_5_data['Dev4_ai7'].tolist()
# water_6 = day_6_data['Dev4_ai7'].tolist()

water = water_1 + water_2 #+ water_3 + water_4 + water_5 + water_6

final_valve_1 = day_1_data['Dev4_ai8'].tolist()
final_valve_2 = day_2_data['Dev4_ai8'].tolist()
# final_valve_3 = day_3_data['Dev4_ai8'].tolist()
# final_valve_4 = day_4_data['Dev4_ai8'].tolist()
# final_valve_5 = day_5_data['Dev4_ai8'].tolist()
# final_valve_6 = day_6_data['Dev4_ai8'].tolist()

final_valve = final_valve_1 + final_valve_2 #+ final_valve_3 + final_valve_4 + final_valve_5 + final_valve_6


cs_plus_yellow_1 = day_1_data['Dev4_ai14'].tolist()
cs_plus_yellow_2 = day_2_data['Dev4_ai14'].tolist()
# cs_plus_yellow_3 = day_3_data['Dev4_ai14'].tolist()
# cs_plus_yellow_4 = day_4_data['Dev4_ai14'].tolist()
# cs_plus_yellow_5 = day_5_data['Dev4_ai14'].tolist()
# cs_plus_yellow_6 = day_6_data['Dev4_ai14'].tolist()

cs_plus_yellow = cs_plus_yellow_1 + cs_plus_yellow_2 #+ cs_plus_yellow_3 + cs_plus_yellow_4 + cs_plus_yellow_5 + cs_plus_yellow_6

cs_plus_orange_1 = day_1_data['Dev4_ai13'].tolist()
cs_plus_orange_2 = day_2_data['Dev4_ai13'].tolist()
# cs_plus_orange_3 = day_3_data['Dev4_ai13'].tolist()
# cs_plus_orange_4 = day_4_data['Dev4_ai13'].tolist()
# cs_plus_orange_5 = day_5_data['Dev4_ai13'].tolist()
# cs_plus_orange_6 = day_6_data['Dev4_ai13'].tolist()

cs_plus_orange  = cs_plus_orange_1 + cs_plus_orange_2 #+ cs_plus_orange_3 + cs_plus_orange_4 + cs_plus_orange_5 + cs_plus_orange_6

cs_minus_brown_1 = day_1_data['Dev4_ai12'].tolist()
cs_minus_brown_2 = day_2_data['Dev4_ai12'].tolist()
# cs_minus_brown_3 = day_3_data['Dev4_ai12'].tolist()
# cs_minus_brown_4 = day_4_data['Dev4_ai12'].tolist()
# cs_minus_brown_5 = day_5_data['Dev4_ai12'].tolist()
# cs_minus_brown_6 = day_6_data['Dev4_ai12'].tolist()

cs_minus_brown = cs_minus_brown_1 + cs_minus_brown_2 #+ cs_minus_brown_3 + cs_minus_brown_4 + cs_minus_brown_5 + cs_minus_brown_6

cs_minus_green_1 = day_1_data['Dev4_ai11'].tolist()
cs_minus_green_2 = day_2_data['Dev4_ai11'].tolist()
# cs_minus_green_3 = day_3_data['Dev4_ai11'].tolist()
# cs_minus_green_4 = day_4_data['Dev4_ai11'].tolist()
# cs_minus_green_5 = day_5_data['Dev4_ai11'].tolist()
# cs_minus_green_6 = day_6_data['Dev4_ai11'].tolist()

cs_minus_green = cs_minus_green_1 + cs_minus_green_2 #+ cs_minus_green_3 + cs_minus_green_4 + cs_minus_green_5 + cs_minus_green_6

odorless_oil_1 = day_1_data['Dev4_ai15'].tolist()
odorless_oil_2 = day_2_data['Dev4_ai15'].tolist()
# odorless_oil_3 = day_3_data['Dev4_ai15'].tolist()
# odorless_oil_4 = day_4_data['Dev4_ai15'].tolist()
# odorless_oil_5 = day_5_data['Dev4_ai15'].tolist()
# odorless_oil_6 = day_6_data['Dev4_ai15'].tolist()

odorless_oil = odorless_oil_1 + odorless_oil_2 #+ odorless_oil_3 + odorless_oil_4 + odorless_oil_5 + odorless_oil_6

yellow_PID_output = []
yellow_motion_sensor_output = []
yellow_camera_trigger_output = []
yellow_laser_output = []
yellow_touch_sensor_output = []
yellow_analog_output_output = []
yellow_water_output = []
yellow_final_valve_output = []
yellow_odorless_oil_output = []
yellow_time_output = []

orange_PID_output = []
orange_motion_sensor_output = []
orange_camera_trigger_output = []
orange_laser_output = []
orange_touch_sensor_output = []
orange_analog_output_output = []
orange_water_output = []
orange_final_valve_output = []
orange_odorless_oil_output = []
orange_time_output = []

green_PID_output = []
green_motion_sensor_output = []
green_camera_trigger_output = []
green_laser_output = []
green_touch_sensor_output = []
green_analog_output_output = []
green_water_output = []
green_final_valve_output = []
green_odorless_oil_output = []
green_time_output = []

brown_PID_output = []
brown_motion_sensor_output = []
brown_camera_trigger_output = []
brown_laser_output = []
brown_touch_sensor_output = []
brown_analog_output_output = []
brown_water_output = []
brown_final_valve_output = []
brown_odorless_oil_output = []
brown_time_output =[]

cs_plus_yellow_output = []
cs_plus_orange_output = []
cs_minus_brown_output = []
cs_minus_green_output = []

yellow_trial_tracker = []
orange_trial_tracker = []
brown_trial_tracker = []
green_trial_tracker = []

water_start = 0

number_of_days = 2
day_count = number_of_days*60

trials = 60 * number_of_days
trial_start = 0

criterion = {}


trial = 0
trial_baseline = 0
trial_range = 25000
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

fliter_by_trial_type = True  #<---------- change to True if you want to output csv files separated by trials with data for all other analog inputs 

while trial < 119: #<----bug
    curr_trial = ""
    for i in range (trial_baseline,trial_range):
        if analog_output[i] > 4.1:
            #print("yes",trial)
            trial_start = i
            trial_end = trial_start + 22000
            break

    curr_trial_type = ""
    for i in range(trial_start, trial_start + 7000):
        #if trial == 27:    
            #print("odor start,odor end:",odor_start,odor_end)
            #print("i:",i)
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
    for i in range(trial_start, trial_end):
        if curr_trial_type == "yellow":
            yellow_PID_output.append(PID[i])
            yellow_motion_sensor_output.append(motion_sensor[i])
            yellow_camera_trigger_output.append(camera_trigger[i])
            yellow_laser_output.append(laser[i])
            yellow_touch_sensor_output.append(touch_sensor[i])
            yellow_analog_output_output.append(analog_output[i])
            yellow_water_output.append(water[i])
            yellow_final_valve_output.append(final_valve[i])
            cs_plus_yellow_output.append(cs_plus_yellow[i])
            yellow_odorless_oil_output.append(odorless_oil[i])
            yellow_time_output.append(time[i])
            yellow_trial_tracker.append(trial)
        if curr_trial_type == "orange":
            orange_PID_output.append(PID[i])
            orange_motion_sensor_output.append(motion_sensor[i])
            orange_camera_trigger_output.append(camera_trigger[i])
            orange_laser_output.append(laser[i])
            orange_touch_sensor_output.append(touch_sensor[i])
            orange_analog_output_output.append(analog_output[i])
            orange_water_output.append(water[i])
            orange_final_valve_output.append(final_valve[i])
            cs_plus_orange_output.append(cs_plus_orange[i])
            orange_odorless_oil_output.append(odorless_oil[i])
            orange_time_output.append(time[i])
            orange_trial_tracker.append(trial)
        if curr_trial_type == "brown":
            brown_PID_output.append(PID[i])
            brown_motion_sensor_output.append(motion_sensor[i])
            brown_camera_trigger_output.append(camera_trigger[i])
            brown_laser_output.append(laser[i])
            brown_touch_sensor_output.append(touch_sensor[i])
            brown_analog_output_output.append(analog_output[i])
            brown_water_output.append(water[i])
            brown_final_valve_output.append(final_valve[i])
            cs_minus_brown_output.append(cs_minus_brown[i])
            brown_odorless_oil_output.append(odorless_oil[i])
            brown_time_output.append(time[i])
            brown_trial_tracker.append(trial)
        if curr_trial_type == "green":
            green_PID_output.append(PID[i])
            green_motion_sensor_output.append(motion_sensor[i])
            green_camera_trigger_output.append(camera_trigger[i])
            green_laser_output.append(laser[i])
            green_touch_sensor_output.append(touch_sensor[i])
            green_analog_output_output.append(analog_output[i])
            green_water_output.append(water[i])
            green_final_valve_output.append(final_valve[i])
            cs_minus_green_output.append(cs_minus_green[i])
            green_odorless_oil_output.append(odorless_oil[i])
            green_time_output.append(time[i])
            green_trial_tracker.append(trial)
    trial_baseline += 22000
    trial_range += 22000
    trial += 1
    print(trial)
        
df1 = pd.DataFrame({'CS+1':cs_plus_yellow_output})
df2 = pd.DataFrame({'CS+2':cs_plus_orange_output})
df3 = pd.DataFrame({'CS-1':cs_minus_brown_output})
df4 = pd.DataFrame({'CS-2':cs_minus_green_output})

df100 = pd.DataFrame({'Time': yellow_time_output})
df101 = pd.DataFrame({'Time': orange_time_output})
df102 = pd.DataFrame({'Time': brown_time_output})
df103 = pd.DataFrame({'Time': green_time_output})




df5 = pd.DataFrame({'PID': yellow_PID_output})
df6 = pd.DataFrame({'motion sensor': yellow_motion_sensor_output})
df7 = pd.DataFrame({'camera trigger': yellow_camera_trigger_output})
df8 = pd.DataFrame({'laser': yellow_laser_output})
df9 = pd.DataFrame({'Touch Sensor': yellow_touch_sensor_output})
df10 = pd.DataFrame({'Analog Output':yellow_analog_output_output})
df11 = pd.DataFrame({'Water': yellow_water_output})
df12 = pd.DataFrame({'Final Valve': yellow_final_valve_output})
df13 = pd.DataFrame({'Odorless oil' : yellow_odorless_oil_output})


df14 = pd.DataFrame({'PID': orange_PID_output})
df15 = pd.DataFrame({'motion sensor': orange_motion_sensor_output})
df16 = pd.DataFrame({'camera trigger': orange_camera_trigger_output})
df17 = pd.DataFrame({'laser': orange_laser_output})
df18 = pd.DataFrame({'Touch Sensor': orange_touch_sensor_output})
df19 = pd.DataFrame({'Analog Output': orange_analog_output_output})
df20 = pd.DataFrame({'Water:': orange_water_output})
df21 = pd.DataFrame({'Final Valve': orange_final_valve_output})
df22 = pd.DataFrame({'Odorless oil' : orange_odorless_oil_output})


df23 = pd.DataFrame({'PID': brown_PID_output})
df24 = pd.DataFrame({'motion sensor': brown_motion_sensor_output})
df25 = pd.DataFrame({'camera trigger': brown_camera_trigger_output})
df26 = pd.DataFrame({'laser': brown_laser_output})
df27 = pd.DataFrame({'Touch Sensor': brown_touch_sensor_output})
df28 = pd.DataFrame({'Analog Output': brown_analog_output_output})
df29 = pd.DataFrame({'Water:': brown_water_output})
df30 = pd.DataFrame({'Final Valve': brown_final_valve_output})
df31 = pd.DataFrame({'Odorless oil' : brown_odorless_oil_output})

df32 = pd.DataFrame({'PID': green_PID_output})
df33 = pd.DataFrame({'motion sensor': green_motion_sensor_output})
df34 = pd.DataFrame({'camera trigger': green_camera_trigger_output})
df35 = pd.DataFrame({'laser': green_laser_output})
df36 = pd.DataFrame({'Touch Sensor': green_touch_sensor_output})
df37 = pd.DataFrame({'Analog Output': green_analog_output_output})
df38 = pd.DataFrame({'Water' : green_water_output})
df39 = pd.DataFrame({'Final Valve': green_final_valve_output})
df40 = pd.DataFrame({'Odorless oil' : green_odorless_oil_output})

df42 = pd.DataFrame({'Trial': yellow_trial_tracker})
df43 = pd.DataFrame({'Trial': orange_trial_tracker})
df44 = pd.DataFrame({'Trial': brown_trial_tracker})
df45 = pd.DataFrame({'Trial': green_trial_tracker})

pd.concat([df100,df1,df5,df6,df7,df8,df9,df10,df11,df12,df13,df42],axis=1).to_csv('cs+1-mouse4-2days.csv', index=False)

pd.concat([df101,df2,df14,df15,df16,df17,df18,df19,df20,df21,df22,df43],axis=1).to_csv('cs+2-mouse4-2days.csv', index=False)

pd.concat([df102,df3,df23,df24,df25,df26,df27,df28,df29,df30,df31,df44],axis=1).to_csv('cs-1-mouse4-2days.csv', index=False)

pd.concat([df103,df4, df32,df33,df34,df35,df36,df37,df38,df39,df40,df45],axis=1).to_csv('cs-2-mouse4-2days.csv', index=False)
