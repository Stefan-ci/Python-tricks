from instaloader import Instaloader

account = input('Enter Instagram username here (copy/paste): ')
Instaloader().download_profile(account, profile_pic_only=False)
