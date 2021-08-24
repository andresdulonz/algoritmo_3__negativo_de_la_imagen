# -*- coding: utf-8 -*-
import cv2
import numpy as np

img_or = cv2.imread('paisaje.jpg')

# Rotación 180
img_rot = cv2.rotate(img_or, cv2.ROTATE_180)

# Unificación y negativización
img_rot_neg = 255 - cv2.cvtColor(img_rot, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagen original', img_or)
cv2.imshow('Imagen negativo rotacion', img_rot_neg)

cv2.waitKey()