
# Quick hack 7.4.2017 mika.nokka1@gmail.com, Jan 2024
# Find mp4 files, use converter for mp3 transformation, show stats
 


import glob
import os
import time

list= glob.glob("*.mp4")
amount=len(list)
print(f"===> Found {amount} mp4 files")
print (f"Files: {list}")
print (f"--------------------------------------------------------------")


start_time = time.time()
counter=0
for items in list:
    counter=counter+1
    mp3=items.replace(".mp4", ".mp3")
    command="ffmpeg -n -i \""+items+"\"  \""+mp3+"\""
    print(f"****************************************************************")
    print(f"*  PROGRESS: {counter}/{amount}")
    print(f"*  FILE: {items}")
    print(f"*  EXECUTING:" + command)
    print (f"****************************************************************")
    os.system(command)
    #ffmpeg -i input.mp4 output.avi

end_time = time.time()
elapsed_time = end_time - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

print(f"===> Processed {amount} mp4 files")
print(f"===> Time taken: {minutes} minutes and {seconds} seconds")
