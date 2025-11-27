from PIL import Image
#import cv2
#import pytesseract


img_file='data.jpg'

im=Image.open(img_file)
#print(im)
#print(im.size)
#im.show()
#im.rotate(90).show()

im.save("Images/data.jpg")