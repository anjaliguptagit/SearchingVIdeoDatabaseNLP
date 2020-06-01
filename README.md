# SearchingVideoDatabaseNLP

'vid_to_aud.py' is the python file that takes the videos from a folder named 'video_files', it converts them to audio files with .wav extension and saves it in 'audio_files' folder.

'split_audio.py' takes the audio files from the 'audio_files' folder and splits them into 5 minute segments each.

'deepspeech_model_exec.py' implements the DeepSpeech pre-trained Speech Recognition model to convert the 5 minute audio segments from each audio to text files.

'keywords' folder contains the algorithm for extracting the keywords from the entire video transcript. We are working on extracting keywords based on the time interval.
