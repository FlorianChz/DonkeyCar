# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:32:56 2022

@author: chaze
"""

import cv2 as cv

img = cv.imread('image_test.jpg')    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("adad", gray)
