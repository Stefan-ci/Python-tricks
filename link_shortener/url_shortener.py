import pyshorteners

url = input("Enter your link please: ")
shortener = pyshorteners.Shortener()
print(shortener.tinyurl.short(url))
