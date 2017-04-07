import glob
list= glob.glob("*.mp4")

for items in list:
    mp3=items.replace(".mp4", ".mp3")
    print("ffmpeg -i "+items +" "+mp3)
    #ffmpeg -i input.mp4 output.avi