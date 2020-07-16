# SearchingVideoDatabaseNLP

Lecture videos are recorded by universities so that they can be used by students to review the courses later. However, usually the lectures are very long, poorly labelled and the required content is hard to find. Specially, sometimes the students want to review a particular topic and its hard to find the lecture and the exact place that it was covered. So, we extract the videos based on the query and find the segment from video that has that keyword.

We have used a pre-trained Speech Recognition model 'DeepSpeech' (https://github.com/mozilla/DeepSpeech) for getting the transcript from the input query and the segmented audio from the NPTEL videos. We filtered it to extract the keywords and also filter the input query transcript to get its keywords. We compared them and got the videos and the time interval depending on the given input query. We have integrated the webpage with the python scripts to display the results after giving query.

'vid_to_aud.py' is the python file that takes the videos from a folder named 'video_files', it converts them to audio files with .wav extension and saves it in 'audio_files' folder.

'split_audio.py' takes the audio files from the 'audio_files' folder and splits them into 5 minute segments each.

'deepspeech_model_exec.py' implements the DeepSpeech pre-trained Speech Recognition model to convert the 5 minute audio segments from each audio to text files and stores it in 'text_files' folder.

'text_to_sheet.py' converts the text files into csv file to be stored in Keywords folder for further processing.

'Keywords' folder contains the algorithm for extracting the keywords from the entire video transcript. We are working on extracting keywords based on the time interval.

'front_end' folder contains the files being used to design the front-end webpage using Django framework to put across queries and display results.
