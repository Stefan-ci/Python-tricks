import geocoder

IP = geocoder.ip('192.168.42.22')
print(f"Your latitude and longitude are: {IP.latlng}")
