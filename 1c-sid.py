# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:32:54 2021

@author: Cristian
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from scipy.interpolate import make_interp_spline

# Read in file for criterion percentages
data = pd.read_csv(r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Processed Data/12-4-criterion-percentages-mouse5-6days.csv")

cs_p1_list = list(data['CS+1'])
cs_p2_list =  list(data['CS+2'])
cs_m1_list = list(data['CS-1'])
cs_m2_list = list(data['CS-2'])

# g1 diff odors 
# g2 cs+ cs- avg + std
# g3 cs+ all mice (halo control)/ cs- all mice (halo control) 
# g4 cs+ halo-control/ cs- halo-control

x_vals = [i for i in range(0, len(cs_p1_list))]

plt.plot(x_vals, cs_p1_list, color = 'yellow')
plt.plot(x_vals, cs_p2_list, color = 'orange')
plt.plot(x_vals, cs_m1_list, color = 'brown')
plt.plot(x_vals, cs_m2_list, color = 'green')
plt.show()

cs_p_list = np.add(cs_p1_list, cs_p2_list)
cs_p_list = [i/2 for i in cs_p_list]
cs_m_list = np.add(cs_m1_list, cs_m2_list)
cs_m_list = [i/2 for i in cs_m_list]

# from plotnine import ggplot, aes, geom_line, geom_smooth

#  df = data.frame(x, y1, y2)
 
#   # melt the data to a long format
#   df2 = melt(data = df, id.vars = "x")
 
#   # plot, using the aesthetics argument 'colour'
#   g = ggplot(data = df2, aes(x = x, y = value, colour = variable)) + geom_line() + geom_smooth()
#   g = g + theme(legend.title = element_blank()) + labs(title = title_name )
#   g = g + scale_color_manual(labels = c("CS+", "CS-"), values = c("darkgreen", "red"))
#   g = g + ylab("% Trials with Licks") + xlab("Trials") + coord_cartesian(ylim = c(0, 100))
#   g = g + geom_hline(yintercept=20, linetype='dotted', col = 'black') +
#     annotate("text", x = 10, y = 20, label = "CS- criterion", vjust = -0.5)
#   g = g + geom_hline(yintercept=80, linetype='dotted', col = 'black') +
#     annotate("text", x = 10, y = 80, label = "CS+ criterion", vjust = -0.5)
#   return (g)


# cs_p_list = data['CS+'].tolist()
# cs_m_list = data['CS-'].tolist()

# trials = []
# trial_start = 20
# for i in range(len(cs_p_list)) :
#     trials.append(trial_start)
#     trial_start+=1

# cs_p_list = np.array(cs_p_list)

# cs_m_list = np.array(cs_m_list)

# trials = np.array(trials)

# x_y_spline_p = make_interp_spline(trials,cs_p_list,k=7)
# x_y_spline_m = make_interp_spline(trials,cs_m_list,k=7)

# x_ = np.linspace(min(trials), max(trials), 200)
# y_p = x_y_spline_p(x_)
# y_m = x_y_spline_m(x_)


# plt.plot(trials,y_p, label='CS+')
# plt.plot(trials,y_m, label='CS-')
# plt.legend()
# plt.show()



# def break_trials(trials, cs):
#     trial_dfs = []
#     for trial in trials:
#         trial_dfs.append(cs[cs['Trial'] == trial])
#     return trial_dfs

# trials_p1 = cs_p1['Trial'].unique()
# trials_p2 = cs_p2['Trial'].unique()
# trials_m1 = cs_m1['Trial'].unique()
# trials_m2 = cs_m2['Trial'].unique()

# # Not incorporated breaking by days yet, but can add that post-hoc
# trial_dfs_p1 = break_trials(trials_p1, cs_p1)
# trial_dfs_p2 = break_trials(trials_p2, cs_p2)
# trial_dfs_m1 = break_trials(trials_m1, cs_m1)
# trial_dfs_m2 = break_trials(trials_m2, cs_m2)

# # COMMENT OUT THIS CODE FOR 2 CHANNELS ON SAME GRAPH (LINES 34 TO 71)
# def plotter(trial_dfs, odor, analog_channel):
#     # incorporate sorting by day
#     # main_fig, axes = plt.subplots(1,4)
#     fig, axs = plt.subplots(len(trial_dfs), sharex= True)
#     fig.suptitle('CS ' + odor)
#     time = range(0, 22000)
#     for i, df in enumerate(trial_dfs):
#         vals = df[analog_channel]
#         axs[i].set_yticks([])
#         axs[i].set_xticks([0, 7000, 9000, 11000, 12000, 22000]) # if you want to remove, can delete 11000
#         axs[i].set_xticklabels(["0s", "7s", "9s", "11s", "12s", "22s"]) # if you delete 11000 above, delete 11s
#         axs[i].set_ylim([0,5]) # this is the limit for the touch sensor voltage, should be changed depending on channel(eg. [0,3] for water)
#         plot_no = i+1
#         axs[i].set_ylabel(plot_no, fontsize= 5, rotation = 0) # make the fontsize smaller for data over more days
#         axs[i].spines["top"].set_visible(False) # Making the frame invisible (these next 4 lines)
#         axs[i].spines["right"].set_visible(False)
#         axs[i].spines["left"].set_visible(False)
#         axs[i].spines["bottom"].set_visible(False) 
#         axs[i].plot(time, vals)   
#     return fig
