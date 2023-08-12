import cv2
import numpy as np

import time

import pathlib

path = str(pathlib.Path(__file__).parent.parent.resolve()) + '/img/test.png'

img = cv2.imread(path)

start = time.time()
w, h, _ = img.shape
cam_center = h // 2, w // 2

# 240, 43, 91
blue = np.uint8([[[255, 0, 0]]]) #here insert the bgr values which you want to convert to hsv
hsvBlue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)

lowerLimit = np.array((hsvBlue[0][0][0] - 10, 100, 100))
upperLimit = np.array((hsvBlue[0][0][0] + 10, 255, 255))

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(img_hsv, lowerLimit, upperLimit)

step = 70
indices = np.argwhere(mask)
indices = indices[::step, :]

distances = np.apply_along_axis(lambda x: np.square(x[0] - cam_center[1]) + np.square(x[1] - cam_center[0]), 1, indices)
closest_ind = np.argmin(distances, axis=0)

delta = 70 // step
forward, backward = max(0, closest_ind - delta), min(len(distances), closest_ind + delta)

end = time.time()

img = cv2.circle(img, center = cam_center, radius = 5, color = (200, 255, 50), thickness = -1, lineType = cv2.LINE_AA) 
img = cv2.circle(img, center = indices[forward][::-1], radius = 5, color = (255, 200, 50), thickness = -1, lineType = cv2.LINE_AA) 

filtered = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)

filtered_img = cv2.cvtColor(filtered, cv2.COLOR_HSV2BGR)

print(f'Time taken for processing: {round((end - start) * 1000, 2)} ms')

## Just project the pixel space waypoint to 3D.
# Get the Projection Matrix of the Camera K
# alpha * [u v 1]' = K(3, 4) [x y z 1]'
# z = height from IMU(known)
# K_new(3, 3) = K[:, :3]
# K_new[:, 2] = K[:, 2] * z + K[:, 3]
# alpha * [u v 1] = K_new(3, 3) [x y 1] (Solve for alpha x y from the 3 equations)
# Send [x y z] as the next waypoint

cv2.imshow('Final', img)
cv2.waitKey(0)
