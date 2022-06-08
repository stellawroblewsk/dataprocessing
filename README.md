# dataprocessing
Necessary Files: 
“criterion_multiple_day.py”
“graphing1bwithfiltering.py”

“criterion_multiple_day.py”: 
To process CSV files (1.containing number of licks on each trial and 2.containing percent correct licks averaged over 20 trials) 
At the top of the file there are multiple lines of code with space to input your chosen files
“Day_x_data = read_csv(“filename of analog data for each consecutive day”)”
After the correct files have been selected, scroll to line 314
Number_of_days = “5” -> for 5 days of data
Lastly, scroll to the bottom of the file (lines 586, 601) and change the output file name to correctly reflect the current mouse and number of days reflected

The program outputs the current trial being processed and finally the criterion values for all 4 stimuli to the print screen
Two CSV files will be created, one documenting an average of correct licks (to change what qualifies as a ‘correct lick’ refer to page 2) over 20 trials for all files inputted and another documenting the number of licks per trial (if you want averages you can make them yourself in excel)
These can then be used to generate graphs etc. 

“graphing1bwithfiltering.py”: 
To process CSV files (Containing the raw analog data separated by stimulus and make 1B) 

At the top of the file there are multiple lines of code with space to input your chosen files
“Day_x_data = read_csv(“filename of analog data for each consecutive day”)”
After the correct files have been selected, scroll to line 393
Number_of_days = “5” -> for 5 days of data
Lastly, perform a search and replace to change the output files to reflect the correct number of days and mouse
The program outputs the current trial being processed and when the program begins to generate figures (as it takes time)
4 CSV files will be created for each stimulus reflecting the filtered analog data (to change how the filtering works refer to page 3)
5 PNGs will be created (one 1B for each stimulus, as well as all four compiled into a single summary image)













To change what qualifies as a ‘correct lick’: 
The lines of code above reflect the portion of the program responsible for the ‘correct lick’ criteria (as well as counting licks per trial)
The current criteria qualifies a correct trial when
CS+: There is a single lick in the 1s time range immediately before water delivery 
CS-: There is no lick in the 1s time range immediately before water delivery 

Line 407 outlines the time range (relative to the analog start of the trial) that is filtered for correct licks (it is currently set to 11000-12000 -> 11-12 s after the start of the trial -> 1 s before water delivery)
Line 411 outlines the number of licks that qualifies as a correct trial (currently set to 1) 





























To alter the filtering method: 
The lines of code above reflect the portion of the program responsible for the filtering criteria
The current criteria excludes trials where 
A CS+ odor is delivered and the mouse does not collect water (lines 481-486)
There is a touch sensor malfunction resulting in a longer pulse than can be expected from a normal lick (lines 462-479)
Line 465 outlines the time range (relative to the analog start of the trial) that is filtered for touch sensor malfunction (it is currently set to 11000-13000 -> 11-13 s after the start of the trial -> 1 s before and after water delivery)
Line 481 outlines the time range (relative to the analog start of the trial) that is checked for collection (currently set to 12-13s -> 1s window following water delivery)
Line 470 outlines how long the pulse must be to be considered a throw away trial (it is currently set to 500, filtering out any touch sensor signal lasting longer than .5 s in the given time range) 
*criterion_multiple_day filters the data in the same way, the only variation is the line number


