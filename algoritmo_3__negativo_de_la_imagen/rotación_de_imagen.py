# -*- coding: utf-8 -*-
import cv2

# Abrir imagen
img = cv2.imread('paisaje.jpg')

# Rotación
img_a = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img_b = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img_c = cv2.rotate(img, cv2.ROTATE_180)

# Mostrar la imagen
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen rotada 90 R', img_a)
cv2.imshow('Imagen rotada 180', img_b)
cv2.imshow('Imagen rotada 90 L', img_c)

# Pausar la ejecución
cv2.waitKey()