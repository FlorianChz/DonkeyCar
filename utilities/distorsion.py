# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:19:08 2022

@author: chaze
"""

import numpy as np
import cv2 as cv
import glob
import pickle 

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((4*6,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:4].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
folder_dir="images_chessboard"
i=0
for iname in glob.glob(f'{folder_dir}/*.jpg'):
    img = cv.imread(iname)    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv.imshow("image en noir et blanc", gray)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (6,4), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        i+=1
        print(i)
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
cv.destroyAllWindows()
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

img = cv.imread('image_test.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))


data = {
        'mtx' : mtx,
        'dist' : dist,
        'newcameramtx' : newcameramtx,
        'roi' : roi
        }

print(data)
with open('calibrate_camera_2.p', 'wb') as f1:
    pickle.dump(data, f1)

