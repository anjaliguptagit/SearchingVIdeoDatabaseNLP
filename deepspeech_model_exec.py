
# running deepspeech model on all audio files if not done already
import os

path1 = 'audio_files/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path1):
    files.extend(d)
    break
# taking all audio files from list called files and applying model onto them if they dont already have corresponding text file

cmd = "deepspeech --model models/output_graph.pbmm --lm models/lm.binary --trie models/trie --audio "

for f in files:
	
	path = 'text_files/'
	# checking if the text file already exists for audio
	if (os.path.exists(path+f)):
		continue

	#otherwise run model on audio file to convert to text file
	else:
		print(path1+f)
		if (os.path.exists(path1+f)):
			#print(cmd+path1+f+" > "+path+f[0:-3]+'txt')
			os.mkdir(path+f)
			i=0
			while(i<20):
				os.system(cmd+path1+f+'/'+str(i)+'.wav'+" > "+path+f+'/'+str(i)+'.txt')
				i+=1
		
	break
