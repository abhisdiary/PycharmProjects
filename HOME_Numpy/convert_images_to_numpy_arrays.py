import cv2

image_grey = cv2.imread("res/smallgray.png", 0)  # 0 means reading the image in greyscale and 1 means reading the image in bgr (blue, green, red)
# print(image_grey)

# Create a new png file
cv2.imwrite("res/newSmallGray.png", image_grey)
