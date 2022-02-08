# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:04:34 2021
@author: Cristian
"""

import pandas as pd
import matplotlib.pyplot as plt
import cv2
from pandas import *
import pandas as pd  
import csv
from itertools import zip_longest
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt

# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220110_13_14_37_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220111_12_22_40_analogData.csv")
# day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220112_12_06_07_analogData.csv")
# day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220113_11_05_52_analogData.csv")
# day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220114_12_36_41_analogData.csv")
# day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220116_12_38_33_analogData.csv")
# day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220117_12_53_40_analogData.csv")
# day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220124_12_46_51_analogData.csv")
# day_7_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220125_11_11_07_analogData.csv")
# day_8_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220126_14_17_14_analogData.csv")
# day_9_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220127_16_39_29_analogData.csv")
# day_10_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220128_14_50_07_analogData.csv")
# day_11_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220130_14_01_42_analogData.csv")
# day_12_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220131_11_58_01_analogData.csv")
# day_13_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220131_14_15_35_analogData.csv")
# day_14_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220201_15_06_01_analogData.csv")
# day_15_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220202_13_34_56_analogData.csv")

day_1_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Analog Data/20220124_15_56_52_analogData.csv")
day_2_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Analog Data/20220125_16_02_59_analogData.csv")
day_3_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Analog Data/20220126_16_48_40_analogData.csv")
day_4_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 24/Analog Data/20220205_16_58_53_analogData.csv")
day_5_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 24/Analog Data/20220206_17_03_07_analogData.csv")
day_6_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 24/Analog Data/20220207_14_07_01_analogData.csv")
day_7_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 24/Analog Data/20220131_11_02_52_analogData.csv")
day_8_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 24/Analog Data/20220131_13_23_18_analogData.csv")
day_9_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 24/Analog Data/20220201_14_39_46_analogData.csv")
day_10_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 24/Analog Data/20220202_13_10_13_analogData.csv")
day_11_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220127_16_39_29_analogData.csv")
day_12_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220128_14_50_07_analogData.csv")
day_13_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220130_14_01_42_analogData.csv")
day_14_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220131_11_58_01_analogData.csv")
day_15_data = read_csv("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 3/Mouse 21/Analog Data/20220131_14_15_35_analogData.csv")

# Read in files cs_p1, cs_p2, cs_m1, cs_m2 for cs+1 cs+2 cs-1 and cs-2 odors respectively

print("files loaded")

time_1 = day_1_data['Time'].tolist()
time_2 = day_2_data['Time'].tolist()
time_3 = day_3_data['Time'].tolist()
time_4 = day_4_data['Time'].tolist()
time_5 = day_5_data['Time'].tolist()
time_6 = day_6_data['Time'].tolist()
time_7 = day_7_data['Time'].tolist()
time_8 = day_8_data['Time'].tolist()
time_9 = day_9_data['Time'].tolist()
time_10 = day_10_data['Time'].tolist()
time_11 = day_11_data['Time'].tolist()
time_12 = day_12_data['Time'].tolist()
time_13 = day_13_data['Time'].tolist()
time_14 = day_14_data['Time'].tolist()
time_15 = day_15_data['Time'].tolist()
time = time_1 + time_2 + time_3 + time_4 + time_5 + time_6 + time_7 + time_8 + time_9 + time_10 + time_11 + time_12 + time_13 + time_14 + time_15

PID_1 = day_1_data['Dev4_ai0'].tolist()
PID_2 = day_2_data['Dev4_ai0'].tolist()
PID_3 = day_3_data['Dev4_ai0'].tolist()
PID_4 = day_4_data['Dev4_ai0'].tolist()
PID_5 = day_5_data['Dev4_ai0'].tolist()
PID_6 = day_6_data['Dev4_ai0'].tolist()
PID_7 = day_7_data['Dev4_ai0'].tolist()
PID_8 = day_8_data['Dev4_ai0'].tolist()
PID_9 = day_9_data['Dev4_ai0'].tolist()
PID_10 = day_10_data['Dev4_ai0'].tolist()
PID_11 = day_11_data['Dev4_ai0'].tolist()
PID_12 = day_12_data['Dev4_ai0'].tolist()
PID_13 = day_13_data['Dev4_ai0'].tolist()
PID_14 = day_14_data['Dev4_ai0'].tolist()
PID_15 = day_15_data['Dev4_ai0'].tolist()
PID = PID_1 + PID_2 + PID_3 + PID_4 + PID_5 + PID_6 + PID_7 + PID_8 + PID_9 + PID_10 + PID_11 + PID_12 + PID_13 + PID_14 + PID_15

motion_sensor_1 = day_1_data['Dev4_ai1'].tolist()
motion_sensor_2 = day_2_data['Dev4_ai1'].tolist()
motion_sensor_3 = day_3_data['Dev4_ai1'].tolist()
motion_sensor_4 = day_4_data['Dev4_ai1'].tolist()
motion_sensor_5 = day_5_data['Dev4_ai1'].tolist()
motion_sensor_6 = day_6_data['Dev4_ai1'].tolist()
motion_sensor_7 = day_7_data['Dev4_ai1'].tolist()
motion_sensor_8 = day_8_data['Dev4_ai1'].tolist()
motion_sensor_9 = day_9_data['Dev4_ai1'].tolist()
motion_sensor_10 = day_10_data['Dev4_ai1'].tolist()
motion_sensor_11 = day_11_data['Dev4_ai1'].tolist()
motion_sensor_12 = day_12_data['Dev4_ai1'].tolist()
motion_sensor_13 = day_13_data['Dev4_ai1'].tolist()
motion_sensor_14 = day_14_data['Dev4_ai1'].tolist()
motion_sensor_15 = day_15_data['Dev4_ai1'].tolist()
motion_sensor = motion_sensor_1 + motion_sensor_2 + motion_sensor_3 + motion_sensor_4 + motion_sensor_5 + motion_sensor_6 + motion_sensor_7 + motion_sensor_8 + motion_sensor_9 + motion_sensor_10 + motion_sensor_11 + motion_sensor_12 + motion_sensor_13 + motion_sensor_14 + motion_sensor_15

camera_trigger_1 = day_1_data['Dev4_ai2'].tolist()
camera_trigger_2 = day_2_data['Dev4_ai2'].tolist()
camera_trigger_3 = day_3_data['Dev4_ai2'].tolist()
camera_trigger_4 = day_4_data['Dev4_ai2'].tolist()
camera_trigger_5 = day_5_data['Dev4_ai2'].tolist()
camera_trigger_6 = day_6_data['Dev4_ai2'].tolist()
camera_trigger_7 = day_7_data['Dev4_ai2'].tolist()
camera_trigger_8 = day_8_data['Dev4_ai2'].tolist()
camera_trigger_9 = day_9_data['Dev4_ai2'].tolist()
camera_trigger_10 = day_10_data['Dev4_ai2'].tolist()
camera_trigger_11 = day_11_data['Dev4_ai2'].tolist()
camera_trigger_12 = day_12_data['Dev4_ai2'].tolist()
camera_trigger_13 = day_13_data['Dev4_ai2'].tolist()
camera_trigger_14 = day_14_data['Dev4_ai2'].tolist()
camera_trigger_15 = day_15_data['Dev4_ai2'].tolist()
camera_trigger = camera_trigger_1 + camera_trigger_2 + camera_trigger_3 + camera_trigger_4 + camera_trigger_5 + camera_trigger_6 + camera_trigger_7 + camera_trigger_8 + camera_trigger_9 + camera_trigger_10 + camera_trigger_11 + camera_trigger_12 + camera_trigger_13 + camera_trigger_14 + camera_trigger_15

laser_1 = day_1_data['Dev4_ai3'].tolist()
laser_2 = day_2_data['Dev4_ai3'].tolist()
laser_3 = day_3_data['Dev4_ai3'].tolist()
laser_4 = day_4_data['Dev4_ai3'].tolist()
laser_5 = day_5_data['Dev4_ai3'].tolist()
laser_6 = day_6_data['Dev4_ai3'].tolist()
laser_7 = day_7_data['Dev4_ai3'].tolist()
laser_8 = day_8_data['Dev4_ai3'].tolist()
laser_9 = day_9_data['Dev4_ai3'].tolist()
laser_10 = day_10_data['Dev4_ai3'].tolist()
laser_11 = day_11_data['Dev4_ai3'].tolist()
laser_12 = day_12_data['Dev4_ai3'].tolist()
laser_13 = day_13_data['Dev4_ai3'].tolist()
laser_14 = day_14_data['Dev4_ai3'].tolist()
laser_15 = day_15_data['Dev4_ai3'].tolist()
laser = laser_1 + laser_2 + laser_3 + laser_4 + laser_5 + laser_6 + laser_7 + laser_8 + laser_9 + laser_10 + laser_11 + laser_12 + laser_13 + laser_14 + laser_15

touch_sensor_1 = day_1_data['Dev4_ai4'].tolist()
touch_sensor_2 = day_2_data['Dev4_ai4'].tolist()
touch_sensor_3 = day_3_data['Dev4_ai4'].tolist()
touch_sensor_4 = day_4_data['Dev4_ai4'].tolist()
touch_sensor_5 = day_5_data['Dev4_ai4'].tolist()
touch_sensor_6 = day_6_data['Dev4_ai4'].tolist()
touch_sensor_7 = day_7_data['Dev4_ai4'].tolist()
touch_sensor_8 = day_8_data['Dev4_ai4'].tolist()
touch_sensor_9 = day_9_data['Dev4_ai4'].tolist()
touch_sensor_10 = day_10_data['Dev4_ai4'].tolist()
touch_sensor_11 = day_11_data['Dev4_ai4'].tolist()
touch_sensor_12 = day_12_data['Dev4_ai4'].tolist()
touch_sensor_13 = day_13_data['Dev4_ai4'].tolist()
touch_sensor_14 = day_14_data['Dev4_ai4'].tolist()
touch_sensor_15 = day_15_data['Dev4_ai4'].tolist()
touch_sensor = touch_sensor_1 + touch_sensor_2 + touch_sensor_3 + touch_sensor_4 + touch_sensor_5 + touch_sensor_6 + touch_sensor_7 + touch_sensor_8 + touch_sensor_9 + touch_sensor_10 + touch_sensor_11 + touch_sensor_12 + touch_sensor_13 + touch_sensor_14 + touch_sensor_15

analog_output_1 = day_1_data['Dev4_ai5'].tolist()
analog_output_2 = day_2_data['Dev4_ai5'].tolist()
analog_output_3 = day_3_data['Dev4_ai5'].tolist()
analog_output_4 = day_4_data['Dev4_ai5'].tolist()
analog_output_5 = day_5_data['Dev4_ai5'].tolist()
analog_output_6 = day_6_data['Dev4_ai5'].tolist()
analog_output_7 = day_7_data['Dev4_ai5'].tolist()
analog_output_8 = day_8_data['Dev4_ai5'].tolist()
analog_output_9 = day_9_data['Dev4_ai5'].tolist()
analog_output_10 = day_10_data['Dev4_ai5'].tolist()
analog_output_11 = day_11_data['Dev4_ai5'].tolist()
analog_output_12 = day_12_data['Dev4_ai5'].tolist()
analog_output_13 = day_13_data['Dev4_ai5'].tolist()
analog_output_14 = day_14_data['Dev4_ai5'].tolist()
analog_output_15 = day_15_data['Dev4_ai5'].tolist()
analog_output = analog_output_1 + analog_output_2 + analog_output_3 + analog_output_4 + analog_output_5 + analog_output_6 + analog_output_7 + analog_output_8 + analog_output_9 + analog_output_10 + analog_output_11 + analog_output_12 + analog_output_13 + analog_output_14 + analog_output_15

water_1 = day_1_data['Dev4_ai7'].tolist()
water_2 = day_2_data['Dev4_ai7'].tolist()
water_3 = day_3_data['Dev4_ai7'].tolist()
water_4 = day_4_data['Dev4_ai7'].tolist()
water_5 = day_5_data['Dev4_ai7'].tolist()
water_6 = day_6_data['Dev4_ai7'].tolist()
water_7 = day_7_data['Dev4_ai7'].tolist()
water_8 = day_8_data['Dev4_ai7'].tolist()
water_9 = day_9_data['Dev4_ai7'].tolist()
water_10 = day_10_data['Dev4_ai7'].tolist()
water_11 = day_11_data['Dev4_ai7'].tolist()
water_12 = day_12_data['Dev4_ai7'].tolist()
water_13 = day_13_data['Dev4_ai7'].tolist()
water_14 = day_14_data['Dev4_ai7'].tolist()
water_15 = day_15_data['Dev4_ai7'].tolist()
water = water_1 + water_2 + water_3 + water_4 + water_5 + water_6 + water_7 + water_8 + water_9 + water_10 + water_11 + water_12 + water_13 + water_14 + water_15

final_valve_1 = day_1_data['Dev4_ai8'].tolist()
final_valve_2 = day_2_data['Dev4_ai8'].tolist()
final_valve_3 = day_3_data['Dev4_ai8'].tolist()
final_valve_4 = day_4_data['Dev4_ai8'].tolist()
final_valve_5 = day_5_data['Dev4_ai8'].tolist()
final_valve_6 = day_6_data['Dev4_ai8'].tolist()
final_valve_7 = day_7_data['Dev4_ai8'].tolist()
final_valve_8 = day_8_data['Dev4_ai8'].tolist()
final_valve_9 = day_9_data['Dev4_ai8'].tolist()
final_valve_10 = day_10_data['Dev4_ai8'].tolist()
final_valve_11 = day_11_data['Dev4_ai8'].tolist()
final_valve_12 = day_12_data['Dev4_ai8'].tolist()
final_valve_13 = day_13_data['Dev4_ai8'].tolist()
final_valve_14 = day_14_data['Dev4_ai8'].tolist()
final_valve_15 = day_15_data['Dev4_ai8'].tolist()
final_valve = final_valve_1 + final_valve_2 + final_valve_3 + final_valve_4 + final_valve_5 + final_valve_6 + final_valve_7 + final_valve_8 + final_valve_9 + final_valve_10 + final_valve_11 + final_valve_12 + final_valve_13 + final_valve_14 + final_valve_15

cs_plus_yellow_1 = day_1_data['Dev4_ai14'].tolist()
cs_plus_yellow_2 = day_2_data['Dev4_ai14'].tolist()
cs_plus_yellow_3 = day_3_data['Dev4_ai14'].tolist()
cs_plus_yellow_4 = day_4_data['Dev4_ai14'].tolist()
cs_plus_yellow_5 = day_5_data['Dev4_ai14'].tolist()
cs_plus_yellow_6 = day_6_data['Dev4_ai14'].tolist()
cs_plus_yellow_7 = day_7_data['Dev4_ai14'].tolist()
cs_plus_yellow_8 = day_8_data['Dev4_ai14'].tolist()
cs_plus_yellow_9 = day_9_data['Dev4_ai14'].tolist()
cs_plus_yellow_10 = day_10_data['Dev4_ai14'].tolist()
cs_plus_yellow_11 = day_11_data['Dev4_ai14'].tolist()
cs_plus_yellow_12 = day_12_data['Dev4_ai14'].tolist()
cs_plus_yellow_13 = day_13_data['Dev4_ai14'].tolist()
cs_plus_yellow_14 = day_14_data['Dev4_ai14'].tolist()
cs_plus_yellow_15 = day_15_data['Dev4_ai14'].tolist()
cs_plus_yellow = cs_plus_yellow_1 + cs_plus_yellow_2 + cs_plus_yellow_3 + cs_plus_yellow_4 + cs_plus_yellow_5 + cs_plus_yellow_6 + cs_plus_yellow_7 + cs_plus_yellow_8 + cs_plus_yellow_9 + cs_plus_yellow_10 + cs_plus_yellow_11 + cs_plus_yellow_12 + cs_plus_yellow_13 + cs_plus_yellow_13 + cs_plus_yellow_14

cs_plus_orange_1 = day_1_data['Dev4_ai13'].tolist()
cs_plus_orange_2 = day_2_data['Dev4_ai13'].tolist()
cs_plus_orange_3 = day_3_data['Dev4_ai13'].tolist()
cs_plus_orange_4 = day_4_data['Dev4_ai13'].tolist()
cs_plus_orange_5 = day_5_data['Dev4_ai13'].tolist()
cs_plus_orange_6 = day_6_data['Dev4_ai13'].tolist()
cs_plus_orange_7 = day_7_data['Dev4_ai13'].tolist()
cs_plus_orange_8 = day_8_data['Dev4_ai13'].tolist()
cs_plus_orange_9 = day_9_data['Dev4_ai13'].tolist()
cs_plus_orange_10 = day_10_data['Dev4_ai13'].tolist()
cs_plus_orange_11 = day_11_data['Dev4_ai13'].tolist()
cs_plus_orange_12 = day_12_data['Dev4_ai13'].tolist()
cs_plus_orange_13 = day_13_data['Dev4_ai13'].tolist()
cs_plus_orange_14 = day_14_data['Dev4_ai13'].tolist()
cs_plus_orange_15 = day_15_data['Dev4_ai13'].tolist()
cs_plus_orange  = cs_plus_orange_1 + cs_plus_orange_2 + cs_plus_orange_3 + cs_plus_orange_4 + cs_plus_orange_5 + cs_plus_orange_6 + cs_plus_orange_7 + cs_plus_orange_8 + cs_plus_orange_9 + cs_plus_orange_10 + cs_plus_orange_11 + cs_plus_orange_12 + cs_plus_orange_13 + cs_plus_orange_14 + cs_plus_orange_15

cs_minus_brown_1 = day_1_data['Dev4_ai12'].tolist()
cs_minus_brown_2 = day_2_data['Dev4_ai12'].tolist()
cs_minus_brown_3 = day_3_data['Dev4_ai12'].tolist()
cs_minus_brown_4 = day_4_data['Dev4_ai12'].tolist()
cs_minus_brown_5 = day_5_data['Dev4_ai12'].tolist()
cs_minus_brown_6 = day_6_data['Dev4_ai12'].tolist()
cs_minus_brown_7 = day_7_data['Dev4_ai12'].tolist()
cs_minus_brown_8 = day_8_data['Dev4_ai12'].tolist()
cs_minus_brown_9 = day_9_data['Dev4_ai12'].tolist()
cs_minus_brown_10 = day_10_data['Dev4_ai12'].tolist()
cs_minus_brown_11 = day_11_data['Dev4_ai12'].tolist()
cs_minus_brown_12 = day_12_data['Dev4_ai12'].tolist()
cs_minus_brown_13 = day_13_data['Dev4_ai12'].tolist()
cs_minus_brown_14 = day_14_data['Dev4_ai12'].tolist()
cs_minus_brown_15 = day_15_data['Dev4_ai12'].tolist()
cs_minus_brown = cs_minus_brown_1 + cs_minus_brown_2 + cs_minus_brown_3 + cs_minus_brown_4 + cs_minus_brown_5 + cs_minus_brown_6 + cs_minus_brown_7 + cs_minus_brown_8 + cs_minus_brown_9 + cs_minus_brown_10 + cs_minus_brown_11 + cs_minus_brown_12 + cs_minus_brown_13 + cs_minus_brown_14 + cs_minus_brown_15

cs_minus_green_1 = day_1_data['Dev4_ai11'].tolist()
cs_minus_green_2 = day_2_data['Dev4_ai11'].tolist()
cs_minus_green_3 = day_3_data['Dev4_ai11'].tolist()
cs_minus_green_4 = day_4_data['Dev4_ai11'].tolist()
cs_minus_green_5 = day_5_data['Dev4_ai11'].tolist()
cs_minus_green_6 = day_6_data['Dev4_ai11'].tolist()
cs_minus_green_7 = day_7_data['Dev4_ai11'].tolist()
cs_minus_green_8 = day_8_data['Dev4_ai11'].tolist()
cs_minus_green_9 = day_9_data['Dev4_ai11'].tolist()
cs_minus_green_10 = day_10_data['Dev4_ai11'].tolist()
cs_minus_green_11 = day_11_data['Dev4_ai11'].tolist()
cs_minus_green_12 = day_12_data['Dev4_ai11'].tolist()
cs_minus_green_13 = day_13_data['Dev4_ai11'].tolist()
cs_minus_green_14 = day_14_data['Dev4_ai11'].tolist()
cs_minus_green_15 = day_15_data['Dev4_ai11'].tolist()
cs_minus_green = cs_minus_green_1 + cs_minus_green_2 + cs_minus_green_3 + cs_minus_green_4 + cs_minus_green_5 + cs_minus_green_6 + cs_minus_green_7 + cs_minus_green_8 + cs_minus_green_9 + cs_minus_green_10 + cs_minus_green_11 + cs_minus_green_12 + cs_minus_green_13 + cs_minus_green_14 + cs_minus_green_15

odorless_oil_1 = day_1_data['Dev4_ai15'].tolist()
odorless_oil_2 = day_2_data['Dev4_ai15'].tolist()
odorless_oil_3 = day_3_data['Dev4_ai15'].tolist()
odorless_oil_4 = day_4_data['Dev4_ai15'].tolist()
odorless_oil_5 = day_5_data['Dev4_ai15'].tolist()
odorless_oil_6 = day_6_data['Dev4_ai15'].tolist()
odorless_oil_7 = day_7_data['Dev4_ai15'].tolist()
odorless_oil_8 = day_8_data['Dev4_ai15'].tolist()
odorless_oil_9 = day_9_data['Dev4_ai15'].tolist()
odorless_oil_10 = day_10_data['Dev4_ai15'].tolist()
odorless_oil_11 = day_11_data['Dev4_ai15'].tolist()
odorless_oil_12 = day_12_data['Dev4_ai15'].tolist()
odorless_oil_13 = day_13_data['Dev4_ai15'].tolist()
odorless_oil_14 = day_14_data['Dev4_ai15'].tolist()
odorless_oil_15 = day_15_data['Dev4_ai15'].tolist()
odorless_oil = odorless_oil_1 + odorless_oil_2 + odorless_oil_3 + odorless_oil_4 + odorless_oil_5 + odorless_oil_6 + odorless_oil_7 + odorless_oil_8 + odorless_oil_9 + odorless_oil_10 + odorless_oil_11 + odorless_oil_12 + odorless_oil_13 + odorless_oil_14 + odorless_oil_15

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

number_of_days = 3
day_count = number_of_days*60

trials = 60 * number_of_days
trial_start = 0

criterion = {}
trial_incl = list(range(0,trials))
#trial_excl =[]

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

#while trial < (day_count - 1): #<----bug
for k in range(0,len(trial_incl)-1) :
    curr_trial = ""
    #if ((k in trial_excl) == False):    
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
        elif (analog_output[i] > 3.3 and analog_output[i]<3.7):
            green_index += 1
            curr_trial_type = "green"
            break
        elif (analog_output[i] > 2.8 and analog_output[i]<3.2):
            brown_index += 1
            curr_trial_type = "brown"
            break
    ##########Filtering out trials with long touch sensor content in the 1 s before water 1s after water time range##########    
    is_lick = False
    time_count = 0
    throw_out = False
    for j in range (trial_start + 11000, trial_start + 13000):
        if time_count < 500:
            if touch_sensor[j] > 1:
                time_count = time_count + 1
                is_lick = True
                if time_count >= 500:
                    throw_out = True       
            elif touch_sensor[j] < 1:
                is_lick = False
                time_count = 0
        else:
            throw_out = True
            break 
   
    collection = False
    
    for j in range (trial_start + 12000, trial_start + 13000):
        if (touch_sensor[j] > 1) and (curr_trial_type == "orange" or curr_trial_type == "yellow"):
            collection = True
            break
    if curr_trial_type == "brown" or curr_trial_type == "green":
        collection = True
    # if throw_out == True:
    #     print("bad trial detected, trial number ", trial, "trial type = ", curr_trial_type)
    first_day = False
    if(throw_out == False and collection == True) or (first_day == True):
        
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
    
    if throw_out == False:
       trial+=1
    
    trial_baseline += 22000
    trial_range += 22000
    #trial += 1
    print(trial)

print("creating data frames...")        
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

pd.concat([df100,df1,df5,df6,df7,df8,df9,df10,df11,df12,df13,df42],axis=1).to_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs+1-mouse 20-filter_collection_3_days.csv', index=False)
cs_p1 = read_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs+1-mouse 20-filter_collection_3_days.csv')

pd.concat([df101,df2,df14,df15,df16,df17,df18,df19,df20,df21,df22,df43],axis=1).to_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs+2-mouse 20-filter_collection_3_days.csv', index=False)
cs_p2 = read_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs+2-mouse 20-filter_collection_3_days.csv')

pd.concat([df102,df3,df23,df24,df25,df26,df27,df28,df29,df30,df31,df44],axis=1).to_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs-1-mouse 20-filter_collection_3_days.csv', index=False)
cs_m1 = read_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs-1-mouse 20-filter_collection_3_days.csv')

pd.concat([df103,df4, df32,df33,df34,df35,df36,df37,df38,df39,df40,df45],axis=1).to_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs-2-mouse 20-filter_collection_3_days.csv', index=False)
cs_m2 = read_csv('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs-2-mouse 20-filter_collection_3_days.csv')

# cs_p1 = pd.read_csv(r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 16/Processed Data/cs+1-mouse11-last3days.csv")
# cs_p2 = pd.read_csv(r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 16/Processed Data/cs+2-mouse11-last3days.csv")
# cs_m1 = pd.read_csv(r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 16/Processed Data/cs-1-mouse11-last3days.csv")
# cs_m2 = pd.read_csv(r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 16/Processed Data/cs-2-mouse11-last3days.csv")


def break_trials(trials, cs):
    trial_dfs = []
    for trial in trials:
        trial_dfs.append(cs[cs['Trial'] == trial])
    return trial_dfs

trials_p1 = cs_p1['Trial'].unique()
trials_p2 = cs_p2['Trial'].unique()
trials_m1 = cs_m1['Trial'].unique()
trials_m2 = cs_m2['Trial'].unique()

# Not incorporated breaking by days yet, but can add that post-hoc
trial_dfs_p1 = break_trials(trials_p1, cs_p1)
trial_dfs_p2 = break_trials(trials_p2, cs_p2)
trial_dfs_m1 = break_trials(trials_m1, cs_m1)
trial_dfs_m2 = break_trials(trials_m2, cs_m2)

# COMMENT OUT THIS CODE FOR 2 CHANNELS ON SAME GRAPH (LINES 34 TO 71)
def plotter(trial_dfs, odor, analog_channel):
    # incorporate sorting by day
    # main_fig, axes = plt.subplots(1,4)
    fig, axs = plt.subplots(len(trial_dfs), sharex= True)
    fig.suptitle('CS ' + odor)
    time = range(0, 22000)
    for i, df in enumerate(trial_dfs):
        vals = df[analog_channel]
        axs[i].set_yticks([])
        axs[i].set_xticks([0, 7000, 9000, 11000, 12000, 22000]) # if you want to remove, can delete 11000
        axs[i].set_xticklabels(["0s", "7s", "9s", "11s", "12s", "22s"]) # if you delete 11000 above, delete 11s
        axs[i].set_ylim([0,5]) # this is the limit for the touch sensor voltage, should be changed depending on channel(eg. [0,3] for water)
        plot_no = i+1
        axs[i].set_ylabel(plot_no, fontsize= 5, rotation = 0) # make the fontsize smaller for data over more days
        axs[i].spines["top"].set_visible(False) # Making the frame invisible (these next 4 lines)
        axs[i].spines["right"].set_visible(False)
        axs[i].spines["left"].set_visible(False)
        axs[i].spines["bottom"].set_visible(False)
        axs[i].plot(time, vals)
    return fig
print("Plotting figures...")
# Here in the last argument, you can pass in another channel (like water/motion sensor/...)
# The last argument name must correspond exactly to the name of one of the columns in the csv file
fig1 = plotter(trial_dfs_p1, '+1', 'Touch Sensor')
fig1.set_size_inches(12.8, 9.6) # doubled default figure size in inches which was (6.4, 4.8) for higher res
fig1.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs+1-mouse 20-filter_collection_3_days.png', dpi=300)

fig2 = plotter(trial_dfs_p2, '+2', 'Touch Sensor')
fig2.set_size_inches(12.8, 9.6) # doubled default figure size in inches which was (6.4, 4.8) for higher res
fig2.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs+2-mouse 20-filter_collection_3_days.png', dpi=300)

fig3 = plotter(trial_dfs_m1, '-1', 'Touch Sensor')
fig3.set_size_inches(12.8, 9.6) # doubled default figure size in inches which was (6.4, 4.8) for higher res
fig3.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs-1-mouse 20-filter_collection_3_days.png', dpi=300)

fig4 = plotter(trial_dfs_m2, '-2', 'Touch Sensor')
fig4.set_size_inches(12.8, 9.6) # doubled default figure size in inches which was (6.4, 4.8) for higher res
fig4.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs-2-mouse 20-filter_collection_3_days.png', dpi=300)


im1 = cv2.imread('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs+1-mouse 20-filter_collection_3_days.png')
im2 = cv2.imread('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs+2-mouse 20-filter_collection_3_days.png')
im3 = cv2.imread('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs-1-mouse 20-filter_collection_3_days.png')
im4 = cv2.imread('C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/cs-2-mouse 20-filter_collection_3_days.png')

im_1 = cv2.vconcat([im1,im2])
im_2 = cv2.vconcat([im3,im4])
im_3 = cv2.hconcat([im_1,im_2])
cv2.imwrite("C:/Users/crist/Dropbox/11-2021_Discrimination/Exp 4/mouse 20/Processed Data/1b-mouse 20-filter_collection_3_days.jpg",im_3)
print("Done!")






