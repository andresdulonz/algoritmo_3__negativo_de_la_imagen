# -*- coding: utf-8 -*-
import cv2
import numpy as np

img_o = cv2.imread('paisaje.jpg')

# Rotación
img_r = cv2.rotate(img_o, cv2.ROTATE_90_CLOCKWISE)

# Inversión de color
img_r_n = 255 - cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagen origina', img_o)
cv2.imshow('Imagen rotada grises negativo', img_r_n)
cv2.waitKey()