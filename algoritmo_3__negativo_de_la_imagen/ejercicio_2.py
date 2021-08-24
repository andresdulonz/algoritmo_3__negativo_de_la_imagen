# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('paisaje.jpg')

# Negativo imagen
img_neg = 255 - img

cv2.imshow('Imagen original', img)
cv2.imshow('Imagen negativo', img_neg)

cv2.waitKey()