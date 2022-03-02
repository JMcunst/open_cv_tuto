# 히스토그램 비교 (histo_compare.py)
import globals
import cv2, numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('images/KakaoTalk_20220223_133738792_02.jpg')
img_ban = cv2.imread('crops/HROML_N4D0004_B_L.jpg')
img_ban2 = cv2.imread('crops/HROML_N5L0003_B_R.jpg')
img_tar = cv2.imread('crops/HROML_N4D0006_L.jpg')

image_crop1 = img1[globals.RARENA_START_Y1:globals.RARENA_END_Y1,globals.RARENA_START_X1:globals.RARENA_END_X1,:]
image_crop4 = img1[globals.RARENA_START_Y4:globals.RARENA_END_Y4,globals.RARENA_START_X1:globals.RARENA_END_X1,:]
image_crop6 = img1[globals.RARENA_START_Y1:globals.RARENA_END_Y1,globals.RARENA_START_X2:globals.RARENA_END_X2,:]

cv2.imshow('query', img1)
imgs = [image_crop1, img_tar]
hists = []
for i, img in enumerate(imgs) :
    plt.subplot(1,len(imgs),i+1)
    plt.title('img%d'% (i+1))
    plt.axis('off') 
    plt.imshow(img[:,:,::-1])
    #---① 각 이미지를 HSV로 변환
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #---② H,S 채널에 대한 히스토그램 계산
    hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
    #---③ 0~1로 정규화
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
    hists.append(hist)


query = hists[0]
methods = {'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 'INTERSECT':cv2.HISTCMP_INTERSECT, 'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}
for j, (name, flag) in enumerate(methods.items()):
    print('%-10s'%name, end='\t')
    for i, (hist, img) in enumerate(zip(hists, imgs)):
        #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
        ret = cv2.compareHist(query, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
            ret = ret/np.sum(query)        #비교대상으로 나누어 1로 정규화
        print("img%d:%7.2f"% (i+1 , ret), end='\t')
    print()
plt.show()