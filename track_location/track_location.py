import geocoder

IP = geocoder.ip('me')
print(f"Your latitude and longitude are: {IP.latlng}")
