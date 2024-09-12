import cv2
import numpy as np

# print (cv2.__version__)
 
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

# img_1 = cv2.imread(r"saved-images\black-image.jpg")
# img_2 = cv2.imread(r"saved-images\Dog.jpg")
# #params of resize: (source, dimensions)
# img_2 = cv2.resize(img_2, (img_1.shape[1], img_1.shape[0]))

# img_3 = img_1 + img_2

# cv2.imshow("Image 1", img_1)
# cv2.imshow("Image 2", img_2)
# cv2.imshow("Added Images", img_3)





#creating 2 black images with dots and adding them
#then connecting the dots between the two lines on the added image
# img_1 = np.zeros((255, 255, 3))
# img_2 = np.zeros((255, 255, 3))
# textImg = np.zeros((255, 255, 3))

# img_1_location = (30, 30)
# img_2_location = (200, 200)
# white = (255, 255, 255)
# smooth_line = cv2.LINE_AA
# font = cv2.FONT_HERSHEY_COMPLEX

# img_1 = cv2.circle(img_1, img_1_location, 1, white, 3)
# img_2 = cv2.circle(img_2, img_2_location, 1, white, 3)
# textImg = cv2.putText(textImg, "Connect the dots", (0, 25), font,
#                       0.75, (255, 255, 255), 1, smooth_line, False)

# img_3 = img_1 + img_2 + textImg
# cv2.line(img_3, img_1_location, img_2_location, white, 1, smooth_line)

# cv2.imshow("Image 1", img_1)
# cv2.imshow("Image 2", img_2)
# cv2.imshow("Added images", img_3)





#Alpha add weighted (stacking 2 slightly transparent images)

# background = cv2.imread(r"saved-images\Beach-Background.jpg")
# background = cv2.resize(background, (500, 500))
# foreground = cv2.imread(r"saved-images\Dog.jpg")
# foreground = cv2.resize(foreground, background.shape[1::-1])

# backgroundAlpha = .7
# foregroundAlpha = 1 - backgroundAlpha

# blendedImg = cv2.addWeighted(background, backgroundAlpha, foreground, foregroundAlpha, 0)
# cv2.imwrite(r"saved-images/blended-image.jpg", blendedImg)

# finalBlendedImage = cv2.imread(r"saved-images\blended-image.jpg")

# cv2.imshow("Blended Image", finalBlendedImage)


#adding an alpha chaannel to an image

# duck = cv2.imread(r"duck.png")
# # cv2.imshow("Duck image", duck)

# cv2.waitKey(0)

# if duck.shape[2] == 3:
#     print("Adding an alpha channel")
#     #add an alpha channel
#     #how to add an alpha channel(transparency)
#     alphaChannel = np.ones((duck.shape[0], duck.shape[1]), dtype=duck.dtype) * 255   #creates the alpha channel
#     cv2.imshow("Image", alphaChannel)
#     finalImg = cv2.merge([duck, alphaChannel])


#     if finalImg.shape[2] == 4:
#         print("Success!")
#     else:
#         print("Fail")

# else:
#     print("Duck has 4 channels")

# duck = cv2.imread(r"image-thresholding\duck-with-alpha.png", cv2.IMREAD_UNCHANGED)

#Image thresholding



#Alpha blending

#need to get the duck into grayscale
# duck = duck[:, :, 2]
# cv2.imshow("Duck", duck)
# cv2.waitKey(0)





#only works for transparent background. Work on this later
im = cv2.imread("image-thresholding\duck-with-alpha.png", cv2.IMREAD_UNCHANGED) 
_, mask = cv2.threshold(im[:, :, 3], 240, 255, cv2.THRESH_BINARY_INV) 
cv2.imshow('duck.jpg', mask)  



# #define images and resize them to the same size:
# background = cv2.imread(r"saved-images\Beach-Background.jpg")
# background = cv2.resize(background, (500, 500))
# foreground = cv2.imread(r"saved-images\Dog.jpg")
# foreground = cv2.resize(foreground, background.shape[1::-1])
# foregroundAlpha = foreground[:, :, 3]

# cv2.imshow("img", background)

# #creating the alpha mask (black and white img with transparent background)
# # im = cv2.imread(r"saved-images\Dog.jpg", cv2.IMREAD_UNCHANGED)

# _, mask = cv2.threshold(foregroundAlpha, 0, 255, cv2.THRESH_BINARY)

# #threshold function: params: source, in this case our img.
#     #the [:, :, 3] notation denotes that the entire width, entire height, and the third index of the rgba
#     #part will be returned. The third index of the rgba is the alpha. So you get the alpha image of the im
# #0 is the threshold. 255 is the decider is the value is not equal to the threshold. cv2.thresh_binary is 

# cv2.imwrite(r'saved-images\mask.jpg', mask)

# # background = background.astype(float)
# # foreground = foreground.astype(float)




#creating threshold images using the color channels
    #1. convert to grayscale
# spiderman = cv2.imread("spiderman.png")
# spidermanGray = cv2.cvtColor(spiderman, cv2.COLOR_BGR2GRAY)

# _, mask = cv2.threshold(spidermanGray, 220, 255, cv2.THRESH_BINARY)
# cv2.imshow("bruh", mask)
# cv2.imwrite(r"image-thresholding\spiderman.png", mask)






cv2.waitKey(0)
cv2.destroyAllWindows()