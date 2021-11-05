import pywhatkit as kit



def main():
	print("##################################\n")
	print("Convert an image to a ascii art text file\n\n\n")
	image_url = str(input("Enter image path: "))
	ascii_out_txt = str(input("Enter output file name: "))
	kit.image_to_ascii_art(image_url, ascii_out_txt)
	print(f"Image with url {image_url} has been sucessfully converted to ascii art text.\n\nThe file name is {ascii_out_txt}")


main()