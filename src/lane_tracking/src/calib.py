import cv2 
import numpy as np

img = cv2.imread('/home/aryansatpathy/DevStuff/imav/src/lane_tracking/img/IMG20230809212545.jpg')
img = cv2.resize(img, dsize = None, fx = 0.25, fy = 0.25)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

objp = np.zeros((7*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)

retval, corners = cv2.findChessboardCorners(img, (7, 7), flags= cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK)
refinedCorners = cv2.cornerSubPix(gray, corners = corners, winSize = (10, 10), zeroZone = (-1, -1), criteria = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1 ))

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objectPoints = [objp],
                                                   imagePoints = [refinedCorners], 
                                                   imageSize = img.shape[:-1], 
                                                   cameraMatrix = None, 
                                                   distCoeffs = None)

print(mtx)

cv2.drawChessboardCorners(img, (7,7), refinedCorners, True)

cv2.imshow('Image', img)
cv2.waitKey(0)