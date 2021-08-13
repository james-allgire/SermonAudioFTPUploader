import os
from pathlib import Path
from os import path
from datetime import datetime
import datetime

#Directory we need to get to /Users/jamesallgire/Desktop/untitled-2.mp3

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..","..", "jamesallgire/Desktop/"))
checkPath = os.listdir(filepath)
#print(checkPath)

for filename in os.listdir(filepath):
    if filename.endswith('.mp3'):
        #Get the creation date of the mp3 file .st_birthtime is specific to mac and unix systems
        info = datetime.datetime.fromtimestamp(os.stat(filename).st_birthtime)   #.st_ctime gives date modified
        #print(info) #uncomment to see what the raaw number value is for the date of the file
        dateTimeObj = info
        # %a gives us the 3 letter day of the week the file was created
        day_of_week_created = dateTimeObj.strftime("%a")
        # %Y%m%d gives us a 4 digit year 2020 two digit month 01 and two digit year 01
        year_month_day_created = dateTimeObj.strftime("%Y%m%d")
        # %H gives us the a 24 hour time without minutes or seconds
        time_cretaed = dateTimeObj.strftime("%H")
        # %p gives us either AM or PM when the file was created
        ap_pm_created = dateTimeObj.strftime("%p")
        #logic for tags at the end of the file
        if day_of_week_created == "Sun" and int(time_cretaed) < 10 :
            event_tag = "-Sunday School"
        elif day_of_week_created == "Sun" and int(time_cretaed) > 10 and int(time_cretaed) < 12 :
            event_tag = "-Sunday AM"
        elif day_of_week_created == "Sun" and int(time_cretaed) > 12 :
            event_tag = "-Sunday PM"    
        elif day_of_week_created == "Wed" :
            event_tag = "-Midweek Service"
        else :
            event_tag ="-Special Meeting"
        new_filename = year_month_day_created + event_tag + ".mp3"
        print(filename  + " " + day_of_week_created + " " + year_month_day_created + " " + time_cretaed + " " + ap_pm_created + " " + str(info) + " " + event_tag)
        print(new_filename)
        #renames the files 
        os.rename(filename, new_filename)
