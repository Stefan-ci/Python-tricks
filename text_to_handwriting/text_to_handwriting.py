import pywhatkit as kit

text = input("Enter your text to be converted to handwriting: ")
kit.text_to_handwriting(text, "handwriting.png", [100, 80, 250])
