# adding names of video files to the list called files
import os

# remove any spaces or () from names of video files
os.chdir('video_files/')
os.system("rename 's/ //g' *")
os.system("rename 's/\(//g' *")
os.system("rename 's/\)//g' *")
os.chdir("..")

path1 = 'video_files/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path1):
    files.extend(f)
    break
print(files)

# taking all video files from list called files and converting it to audio files with same name as video files

import ffmpy
for f in files:
	
	path = 'audio_files/'
	#if audio file exists, do nothing
	if (os.path.exists(path + f[0:-4] + '.wav')):
		continue

	#otherwise convert this video to audio file of same name
	else:
		os.system("ffmpeg -i " + path1 + f + " " + path + f[0:-4] + ".wav");
