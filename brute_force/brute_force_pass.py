import random
import pyautogui

characters = """0123456789=)_-('&]@^|[#~&=azertyui]opqsdfghjklmwxc
vbnAZERTYUIOPQSDFGHJKLMWXCVBN?$*£%§!/:.;,"""
characters_list = list(characters)
password = pyautogui.password('Enter password here: ')
guess_password = ''
while guess_password != password:
	guess_password = random.choices(characters_list, k=len(password))
	print(f'>>>> Testing {guess_password} <<<<')

	if guess_password == list(password):
		print('='*25)
		print('Eureka!!!!!!\nYour password is ' + ''.join(guess_password))
		print('='*25)
		file = open('guess_password.txt', 'w')
		file.write(str('Password found! It is: ' + ''.join(guess_password)))
		file.close()
		break
