from PIL import Image

#open the image
im1=Image.open('funnel-800.jpg')


print(im1.format, im1.size,im1.mode)

im1.convert('L')

