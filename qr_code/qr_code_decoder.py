from pyzbar.pyzbar import decode
from PIL import Image
decoder = decode(Image.open(input("Enter file path followed by its name: ")))
print(f"Encoded message in the QR Code is: \n\n {decoder[0].data.decode('ascii')}")
