import cv2
import numpy as np
 
'''  imread reads the image from the file given as a parameter
and returns a matrix of pixels
'''

# img = np.zeros((512, 512, 3))
# # cv2.imwrite(r"saved-images/black-image.jpg", img)

# withText = cv2.putText(img, "Hello World", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
# image = cv2.imread(r"saved-images\Dog.jpg")

# reshapedDog = cv2.resize(image, (512, 512))
# # cv2.imshow("Image", image)

# # cv2.imshow("Image", img)





# cv2.waitKey(0)
# #line
# lineStartPoint = (270, 100)
# lineEndPoint = (360, 90)

# #rect
# rectStartPoint = (135, 50)
# rectEndPoint = (500, 180)

# #circ
# circleCenter = (310, 95)
# circleRadius = 30

#polygon
# vertises = [[10, 10], [20, 20], [30, 20], [10, 10]]
# pts = np.array(
#                 [[[25, 70]], [[25, 160]], 
#                 [[110, 200]], [[200, 160]], 
#                 [[200, 70]], [[110, 20]]],
#                )

# pts = pts.reshape((-1, 2, 2))
# print(pts)

# color = (0, 255, 0)
# thickness = (5)
# print(image.shape)

# imageWithLine = cv2.line(image, lineStartPoint, lineEndPoint, color, thickness)
# rectangle = cv2.rectangle(image, rectStartPoint, rectEndPoint, color, thickness )
# circle = cv2.circle(image, circleCenter, circleRadius, color, thickness)
# polylines = cv2.polylines(image, pts, True, color, thickness)



# cv2.destroyAllWindows()







# path = r'images\savedDogGrayCripped.jpg'
# croppedImg = image[0: 300, 0: 700]
# cv2.imwrite(path, croppedImg)
#r makes the string a raw string which means it ignores the backslash good to use for file directories

# croppedImg = image[50: 100, 700: 1500]
#this crops the image. height, width, color channel. 0: 100 means starting from pixel 0 to 100 height
#0: 1500 means starting from 0 pixel to 1500 width have to stay within the size of the image, if the second number
#is greater than the image size, it will just go to the end

'''In the imshow function, the second image parameter is matlike. this is a matrix of pixels
(or just an image) in image processing, the images are saved as a matrix of pixels. in a 2d array,
the image is in grayscale like [[0, 177, 255]
                                [255, 177, 0]], which is a gray img with 2 lines of pixels. 
in a 3d array, the pixels are colored where each pixel is an array of 3 numbers(rgb)
for example: [[[0, 0, 255], [0, 255, 0], [255, 0, 0]],
                [[0, 0, 255], [0, 255, 0], [255, 0, 0]]] two rows of pixels'''
# print(image.shape)
# cv2.imshow("Image", croppedImg)

# cv2.waitKey(0)

# cv2.destroyAllWindows()



#adding and subtracting images:

img_1 = cv2.imread(r"saved-images\black-image.jpg")
img_2 = cv2.imread(r"saved-images\Dog.jpg")
#params of resize: (source, dimensions)
img_2 = cv2.resize(img_2, (img_1.shape[1], img_1.shape[0]))

img_3 = img_1 + img_2

cv2.imshow("Image 1", img_1)
cv2.imshow("Image 2", img_2)
cv2.imshow("Added Images", img_3)

cv2.waitKey(0)
cv2.destroyAllWindows()