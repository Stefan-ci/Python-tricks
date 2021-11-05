import os
import shutil

image_formats = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'tiff']
audio_formats = ['mp3', 'wav', 'aac']
video_formats = ['mp4', 'avi', 'mov', 'webm']
docs_formats = ['ai', 'ait', 'txt', 'doc', 'docx', 'rtf']

while True:
	files = os.listdir('./')

	for file in files:
		if os.path.isfile(file) and file != 'file_organizer_2.py':
			ext = (file.split('.')[-1]).lower()

			if ext in image_formats:
				shutil.move(file, 'images/'+file)
			elif ext in audio_formats:
				shutil.move(file, 'audios/'+file)
			elif ext in video_formats:
				shutil.move(file, 'videos/'+file)
			elif ext in docs_formats:
				shutil.move(file, 'docs/'+file)
			else:
				shutil.move(file, 'others/'+file)

