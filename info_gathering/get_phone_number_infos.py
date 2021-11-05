import phonenumbers
from phonenumbers import geocoder, carrier

phone_number = input('Enter your phone number (with country code): ')
number = phonenumbers.parse(phone_number)

print(geocoder.description_for_number(number, 'fr'))
print(carrier.name_for_number(number, 'fr'))
