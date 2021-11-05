import moviepy.editor as mp

path_to_video = input('Enter video path: \n==>Path: ')
clip = mp.VideoFileClip(path_to_video)
clip.audio.write_audiofile(r"audio.wav")
