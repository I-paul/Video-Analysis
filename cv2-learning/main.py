import cv2
import numpy as np

frame = cv2.imread('.\data\Test\wallpaper1.jpg')
cv2.imshow('Image', frame)

cv2.rectangle(frame, (200,200), (600, 600), (100, 55, 100), 2)
cv2.imshow('Image with Rectangle', frame)

# Hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# Lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
# cv2.imshow('HSV', Hsv)
# cv2.imshow('LAB', Lab)

# Imgx2 = cv2.resize(frame, (0, 0), fx=2, fy=2)
# Img = cv2.resize(frame,(0,0) , fx=1.5, fy=1.5)
# cv2.imshow('Image x2', Imgx2)
# cv2.imshow('Image 1.5x', Img)

# flip = cv2.flip(frame , -1)
# flip2 = cv2.flip(frame , 0)
# flip3 = cv2.flip(frame , 1)
# cv2.imshow('Flipped Image', flip)
# cv2.imshow('Flipped Image 2', flip2)
# cv2.imshow('Flipped Image 3', flip3)

cv2.waitKey(0)