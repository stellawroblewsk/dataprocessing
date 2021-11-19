# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 10:35:22 2021

@author: Cristian
"""
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

PID_1 = day_1_data['Dev4_ai0'].tolist()
PID_2 = day_2_data['Dev4_ai0'].tolist()
PID_3 = day_3_data['Dev4_ai0'].tolist()
PID_4 = day_4_data['Dev4_ai0'].tolist()
PID_5 = day_5_data['Dev4_ai0'].tolist()
PID_6 = day_6_data['Dev4_ai0'].tolist()

PID = PID_1 + PID_2 + PID_3 + PID_4 + PID_5 + PID_6

motion_sensor_1 = day_1_data['Dev4_ai1'].tolist()
motion_sensor_2 = day_2_data['Dev4_ai1'].tolist()
motion_sensor_3 = day_3_data['Dev4_ai1'].tolist()
motion_sensor_4 = day_4_data['Dev4_ai1'].tolist()
motion_sensor_5 = day_5_data['Dev4_ai1'].tolist()
motion_sensor_6 = day_6_data['Dev4_ai1'].tolist()

motion_sensor = motion_sensor_1 + motion_sensor_2 + motion_sensor_3 + motion_sensor_4 + motion_sensor_5 + motion_sensor_6

camera_trigger_1 = day_1_data['Dev4_ai2'].tolist()
camera_trigger_2 = day_2_data['Dev4_ai2'].tolist()
camera_trigger_3 = day_3_data['Dev4_ai2'].tolist()
camera_trigger_4 = day_4_data['Dev4_ai2'].tolist()
camera_trigger_5 = day_5_data['Dev4_ai2'].tolist()
camera_trigger_6 = day_6_data['Dev4_ai2'].tolist()

camera_trigger = camera_trigger_1 + camera_trigger_2 + camera_trigger_3 + camera_trigger_4 + camera_trigger_5 + camera_trigger_6

laser_1 = day_1_data['Dev4_ai3'].tolist()
laser_2 = day_2_data['Dev4_ai3'].tolist()
laser_3 = day_3_data['Dev4_ai3'].tolist()
laser_4 = day_4_data['Dev4_ai3'].tolist()
laser_5 = day_5_data['Dev4_ai3'].tolist()
laser_6 = day_6_data['Dev4_ai3'].tolist()

laser = laser_1 + laser_2 + laser_3 + laser_4 + laser_5 + laser_6


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

final_valve_1 = day_1_data['Dev4_ai8'].tolist()
final_valve_2 = day_2_data['Dev4_ai8'].tolist()
final_valve_3 = day_3_data['Dev4_ai8'].tolist()
final_valve_4 = day_4_data['Dev4_ai8'].tolist()
final_valve_5 = day_5_data['Dev4_ai8'].tolist()
final_valve_6 = day_6_data['Dev4_ai8'].tolist()

final_valve = final_valve_1 + final_valve_2 + final_valve_3 + final_valve_4 + final_valve_5 + final_valve_6


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

odorless_oil_1 = day_1_data['Dev4_ai15'].tolist()
odorless_oil_2 = day_2_data['Dev4_ai15'].tolist()
odorless_oil_3 = day_3_data['Dev4_ai15'].tolist()
odorless_oil_4 = day_4_data['Dev4_ai15'].tolist()
odorless_oil_5 = day_5_data['Dev4_ai15'].tolist()
odorless_oil_6 = day_6_data['Dev4_ai15'].tolist()

odorless_oil = odorless_oil_1 + odorless_oil_2 + odorless_oil_3 + odorless_oil_4 + odorless_oil_5 + odorless_oil_6

yellow_PID_output = []
yellow_motion_sensor_output = []
yellow_camera_trigger_output = []
yellow_laser_output = []
yellow_touch_sensor_output = []
yellow_analog_output_output = []
yellow_water_output = []
yellow_final_valve_output = []
yellow_odorless_oil_output = []

orange_PID_output = []
orange_motion_sensor_output = []
orange_camera_trigger_output = []
orange_laser_output = []
orange_touch_sensor_output = []
orange_analog_output_output = []
orange_water_output = []
orange_final_valve_output = []
orange_odorless_oil_output = []

green_PID_output = []
green_motion_sensor_output = []
green_camera_trigger_output = []
green_laser_output = []
green_touch_sensor_output = []
green_analog_output_output = []
green_water_output = []
green_final_valve_output = []
green_odorless_oil_output = []

brown_PID_output = []
brown_motion_sensor_output = []
brown_camera_trigger_output = []
brown_laser_output = []
brown_touch_sensor_output = []
brown_analog_output_output = []
brown_water_output = []
brown_final_valve_output = []
brown_odorless_oil_output = []

cs_plus_yellow_output = []
cs_plus_orange_output = []
cs_minus_brown_output = []
cs_minus_green_output = []



water_start = 0

number_of_days = 6
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

while trial < 359: #<----bug
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
    trial_baseline += 22000
    trial_range += 22000
    trial += 1
    print(trial)
        
df1 = pd.DataFrame({'CS+1':cs_plus_yellow_output})
df2 = pd.DataFrame({'CS+2':cs_plus_orange_output})
df3 = pd.DataFrame({'CS-1':cs_minus_brown_output})
df4 = pd.DataFrame({'CS-2':cs_minus_green_output})


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




pd.concat([df1,df5,df6,df7,df8,df9,df10,df11,df12,df13],axis=1).to_csv('cs+1-mouse9.csv', index=False)

pd.concat([df2,df14,df15,df16,df17,df18,df19,df20,df21,df22],axis=1).to_csv('cs+2-mouse9.csv', index=False)

pd.concat([df3,df23,df24,df25,df26,df27,df28,df29,df30,df31],axis=1).to_csv('cs-1-mouse9.csv', index=False)

pd.concat([df4, df32,df33,df34,df35,df36,df37,df38,df39,df40],axis=1).to_csv('cs-2-mouse9.csv', index=False)





#     touch_sensor_start =  trial_start + time_from_beginning
#     touch_sensor_end = touch_sensor_start + stop_reading
#     is_lick = False
#     for j in range (touch_sensor_start, touch_sensor_end): 
#         if (touch_sensor[j] > 1) and (is_lick == False):
#             if curr_trial_type == "yellow":
#                # yellow_trials += 1
#                 yellow_licks[yellow_index] += 1
#                 is_lick = True
#             elif curr_trial_type == "orange":
#                # orange_trials += 1
#                 orange_licks[orange_index] += 1
#                 is_lick = True
#             elif curr_trial_type == "brown":
#                 #brown_trials +=1
#                 brown_licks[brown_index] += 1
#                 is_lick = True
#             elif curr_trial_type == "green":
#                # green_trials += 1
#                 green_licks[green_index] += 1
#                 is_lick = True
                
#         elif touch_sensor[j] < 1:
#             is_lick = False
        
#     trial_baseline += 22000
#     trial_range += 22000
#     trial += 1
#     print(trial)

# yellow_licks = [i for i in yellow_licks if i != 0]
# orange_licks =  [i for i in orange_licks if i != 0]
# brown_licks =  [i for i in brown_licks if i != 0]
# green_licks =  [i for i in green_licks if i != 0]

# df1 = pd.DataFrame({'CS+1':yellow_licks})
# df2 = pd.DataFrame({'CS+2':orange_licks})
# df3 = pd.DataFrame({'CS-1':brown_licks})
# df4 = pd.DataFrame({'CS-2':green_licks})
# pd.concat([df1,df2,df3,df4],axis=1).to_csv('4-43-bigfile.csv', index=False)



























#print(len(yellow_licks),len(orange_licks),len(green_licks),len(brown_licks))
# rows = zip(yellow_licks,orange_licks,brown_licks,green_licks)
# with open("C:/Users/crist/Dropbox/criterio_python code/first_graph.csv", "w") as f :
#     writer = csv.writer(f)
#     for row in rows:
#         writer.writerow(row)

# yellow_xs = [x for x in range(len(yellow_licks))]
# plt.show()
# plt.savefig("yellow_plot_1.png")
# plt.close()


#    
#             for j in range (touch_sensor_start, touch_sensor_start + time_offset):
#                 if touch_sensor[i] > 
#                     cs_plus_trials_yellow.append(touch_sensor[j])
           
#         elif (cs_plus_orange[i] > 1):
#             for j in range (touch_sensor_start, touch_sensor_start + time_offset):
#                 cs_plus_trials_orange.append(touch_sensor[j])
                
#         elif (cs_minus_brown[i] > 1):
#             for j in range (touch_sensor_start, touch_sensor_start + time_offset):
#                 cs_minus_trials_brown.append(touch_sensor[j])
                
#         elif (cs_minus_green[i] > 1):
#             for j in range (touch_sensor_start, touch_sensor_start + 5000):
#                 cs_minus_trials_green.append(touch_sensor[j])
#     trial += 1
#     print(trial)

# cs_plus_yellow_y = list(range(0,len(cs_plus_trials_yellow)))

# plt.plot(cs_plus_yellow_y, cs_plus_trials_yellow)
# plt.savefig('mouse31_yellow.png')


# trial = 0
# trial_baseline = 0
# trial_range = 22000

# while trial < day_count:
#     for i in range (trial_baseline,trial_range):
#         if (cs_plus_yellow[i] > 1):
#             trial_type = "yellow_cs+"
#         elif (cs_plus_orange[i] > 1):
#             trial_type = "orange_cs+"
#         elif cs_minus_brown[i] > 1:
#             trial_type = "brown_cs-"
#         elif cs_minus_green[i] > 1:
#             trial_type = "green_cs-"
        
#     trial_baseline += 22000
#     trial_range += 22000
#     value = criterion[trial] + trial_type
#     criterion[trial] = value
#     trial += 1
#     trial_type = ""

# print(criterion)

# cs_plus_trials_yellow = []
# cs_plus_trials_orange = []
# cs_minus_trials_brown = []
# cs_minus_trials_green = []
# for i in criterion:
#     if ("yellow" in criterion[i]):
#         if 'true' in criterion[i]:
#             cs_plus_trials_yellow.append(1)
#         else:
#             cs_plus_trials_yellow.append(0)
#     elif ("orange" in criterion[i]):
#         if 'true' in criterion[i]:
#             cs_plus_trials_orange.append(1)
#         else:
#             cs_plus_trials_orange.append(0)
#     elif ("brown" in criterion[i]):
#         if 'true' in criterion[i]:
#             cs_minus_trials_brown.append(1)
#         else:
#             cs_minus_trials_brown.append(0)
#     elif ("green" in criterion[i]):
#         if 'true' in criterion[i]:
#             cs_minus_trials_green.append(1)
#         else:
#             cs_minus_trials_green.append(0)



# df1 = ({'cs_plus_trials_yellow': cs_plus_trials_yellow})
# df2 = ({'cs_plus_trials_orange': cs_plus_trials_orange})
# df3 = ({'cs_minus_trials_brown': cs_minus_trials_brown})
# df4 = ({ 'cs_minus_trials_green': cs_minus_trials_green})
       
# pd.concat([df1,df2,df3,df4],axis=1).to_csv('Mouse_3_CONSM.csv', index = False)

# d = [cs_plus_trials_yellow,cs_plus_trials_orange,cs_minus_trials_brown,cs_minus_trials_green]

# with open("Mouse_9_CONSM.csv","w+") as f:
#     writer = csv.writer(f)
#     for values in zip_longest(*d):
#         writer.writerow(values)

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


