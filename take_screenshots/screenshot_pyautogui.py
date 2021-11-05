import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def take_screenshot():
	my_screenshot = pyautogui.screenshot()
	file_path = filedialog.asksaveasfilename(defaultextension='.png')
	my_screenshot.save(file_path)

my_button = tk.Button(text='Take a screenshot', command=take_screenshot, 
	bg='black', fg='white', font=10)
canvas1.create_window(150, 150, window=my_button)

root.mainloop()

