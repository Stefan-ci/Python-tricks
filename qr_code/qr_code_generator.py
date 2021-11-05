import pyqrcode

text = input("Enter text to be encoded: ")
qr = pyqrcode.create(text)
qr.png(f"qr_code.png", scale=6)
print("Text encoded sucessfully !")
