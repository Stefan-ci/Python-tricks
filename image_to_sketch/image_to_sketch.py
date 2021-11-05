import cv2


image = cv2.imread('tset_image.png')
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertblur = cv2.bitwise_not(blur)

sketch = cv2.divide(grey, invertblur, scale=260)
cv2.imwrite('sketch_image.png', sketch)
