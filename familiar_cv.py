import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.testing.compare as plttc
import pytesseract
import os
import globals
import func

img1 = cv2.imread('images/KakaoTalk_20220223_133738792_03.jpg')

image_crop1 = img1[globals.RARENA_START_Y1:globals.RARENA_END_Y1,globals.RARENA_START_X1:globals.RARENA_END_X1,:]
image_crop2 = img1[globals.RARENA_START_Y2:globals.RARENA_END_Y2,globals.RARENA_START_X1:globals.RARENA_END_X1,:]
image_crop3 = img1[globals.RARENA_START_Y3:globals.RARENA_END_Y3,globals.RARENA_START_X1:globals.RARENA_END_X1,:]
image_crop4 = img1[globals.RARENA_START_Y4:globals.RARENA_END_Y4,globals.RARENA_START_X1:globals.RARENA_END_X1,:]
image_crop5 = img1[globals.RARENA_START_Y5:globals.RARENA_END_Y5,globals.RARENA_START_X1:globals.RARENA_END_X1,:]
image_crop6 = img1[globals.RARENA_START_Y1:globals.RARENA_END_Y1,globals.RARENA_START_X2:globals.RARENA_END_X2,:]
image_crop7 = img1[globals.RARENA_START_Y2:globals.RARENA_END_Y2,globals.RARENA_START_X2:globals.RARENA_END_X2,:]
image_crop8 = img1[globals.RARENA_START_Y3:globals.RARENA_END_Y3,globals.RARENA_START_X2:globals.RARENA_END_X2,:]
image_crop9 = img1[globals.RARENA_START_Y4:globals.RARENA_END_Y4,globals.RARENA_START_X2:globals.RARENA_END_X2,:]
image_crop10 = img1[globals.RARENA_START_Y5:globals.RARENA_END_Y5,globals.RARENA_START_X2:globals.RARENA_END_X2,:]

image_crop_fb1 = img1[globals.RARENA_FB_STY:globals.RARENA_FB_ENY,globals.RARENA_FB_STX1:globals.RARENA_FB_ENX1,:]
image_crop_fb2 = img1[globals.RARENA_FB_STY:globals.RARENA_FB_ENY,globals.RARENA_FB_STX2:globals.RARENA_FB_ENX2,:]

image_crop_wl = img1[globals.RARENA_WL_STY:globals.RARENA_WL_ENY,globals.RARENA_WL_STX:globals.RARENA_WL_ENX,:]

code1 = func.find_hero(image_crop1, 'L')
code2 = func.find_hero(image_crop2, 'L')
code3 = func.find_hero(image_crop3, 'L')
code4 = func.find_hero(image_crop4, 'L') # ban 보랏츠
code5 = func.find_hero(image_crop5, 'L')
code6 = func.find_hero(image_crop6, 'R') # ban 지릴리
code7 = func.find_hero(image_crop7, 'R')
code8 = func.find_hero(image_crop8, 'R')
code9 = func.find_hero(image_crop9, 'R')
code10 = func.find_hero(image_crop10, 'R')

codefb1 = func.find_hero(image_crop_fb1, 'FB')
codefb2 = func.find_hero(image_crop_fb2, 'FB')

codewl = func.find_hero(image_crop_wl, 'WL')

# plt.imshow(image_crop_wl) 
# plt.show()
# print(code1)
# print(code2)
# print(code3)
# print(code4)
# print(code5)
# print(code6)
# print(code7)
# print(code8)
# print(code9)
# print(code10)
print('나의 픽벤: ', code1, code2, code3, code4, code5)
print('적의 픽벤: ', code6, code7, code8, code9, code10)
print('프리벤:' ,codefb1, codefb2)
print('승리여부:', codewl)