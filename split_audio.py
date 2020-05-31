#ffmpeg -i video_files/Thenextoutbreak_We’renotready_BillGates.mp3  -ss 00:00:00 -codec copy -t 10 video_files/Thenextoutbreak_We’renotready_BillGates/1.mp3
import os
from subprocess import Popen, PIPE
import datetime
import ffmpy
import math

path = 'audio_files/'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    files.extend(f)
    break

for f in files:
	
	# checking if the directory already exists for video
	if (os.path.exists(path+f[0:-4])):
		continue

	#otherwise split this video and add to directory of same name
	else:
		
		os.mkdir(path+f[0:-4])
		
		# output gives the time duration of the video
		comd = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 -sexagesimal "+path+f
		stdout = Popen(comd, shell=True, stdout=PIPE).stdout
		output = stdout.read()
		
		# t is total time hr is hours, m is minutes, sec is seconds for converting to timeframe format
		t = output[:-8]
		hr = int(t[:-6])
		m = int(t[-5:-3])
		sec = int(t[-2:])
		
		#total time of audio
		d1 = datetime.timedelta(seconds=sec, minutes=m, hours=hr)
		
		#start time of clipped audio
		d2 = datetime.timedelta(seconds=0, minutes=0, hours=0)
		
		#end time of clipped audio
		d3 = datetime.timedelta(seconds=0, minutes=5, hours=0)
		print(str(d1))
		print(str(d2))
		i=0
		
		#while endtime < totaltime
		while(d3<d1):
			os.system("ffmpeg -i " + path+f + " -ss "+str(d2)+" -codec copy -t 300 "+path+f[0:-4]+"/"+str(i)+".wav")
			d2 = d2 + datetime.timedelta(seconds=0, minutes=5, hours=0)
			d3 = d3 + datetime.timedelta(seconds=0, minutes=5, hours=0)
			i+=1
		remain = str(math.floor((d1-d2).total_seconds()))
		os.system("ffmpeg -i " + path+f + " -ss "+str(d2)+" -codec copy -t " + remain + ' '+path+f[0:-4]+"/"+str(i)+".wav")
		
		
		

