from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

file_path = askopenfilename()

img = Image.open(file_path)
img_height, img_width = img.size

img = img.resize((img_height, img_width), Image.ANTIALIAS)

save_path = asksaveasfilename()
img.save(save_path)
