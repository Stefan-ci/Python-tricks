from tkinter import Tk, Label, Button
from random import choice


root = Tk()
root.geometry('700x450')
root.title('Dice Roll with Tkinter - Python')

label = Label(root, text='', font=('times', 200))


def roll():
	dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
	label.configure(text=f'{choice(dice)}{choice(dice)}{choice(dice)}')
	label.pack()

button = Button(root, text='Roll', width=10, height=1, font=10, 
	bg='white', bd=2, command=roll)
button.pack(padx=10, pady=10)

root.mainloop()
