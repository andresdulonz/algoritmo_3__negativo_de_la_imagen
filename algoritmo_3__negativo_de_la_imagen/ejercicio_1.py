# -*- coding: utf-8 -*-
import cv2
import numpy as np

img_a = cv2.imread('paisaje.jpg')

# Inversión de color
img_b = 255 - cv2.cvtColor(img_a, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagen original', img_a)
cv2.imshow('Imagen escala grises',img_b)

cv2.waitKey()