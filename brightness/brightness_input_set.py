import screen_brightness_control as sbc

def main():	
	print(f"Current brightness value is {sbc.get_brightness()}")
	new_brightness = int(input("Enter new brightness value: "))
	set_new_brightness = sbc.set_brightness(new_brightness)
	print(f"New brightness value is {sbc.get_brightness()}")
	print("==============================\n")

while True:
	main()

if __name__ == '__main__':
	main()
