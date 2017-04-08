
## Quick hack 7.4.2017 mika.nokka1@gmail.com
#Find mp4 files, use converter for mp3 transformation
#Windows variant


import glob
import os

list= glob.glob("*.mp4")

for items in list:
    mp3=items.replace(".mp4", ".mp3")
    command="ffmpeg -n -i \""+items+"\"  \""+mp3+"\""
    print("****** EXECUTING:" + command)
    os.system(command)
    #ffmpeg -i input.mp4 output.avi
