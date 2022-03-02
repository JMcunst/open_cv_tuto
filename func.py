import cv2
import numpy as np
import matplotlib.pyplot as plt
import hero_code
import globals

ALL_HEROS = [{'code':'HROCM_N3R0001','name':'라스'}, {'code':'HROCM_Y3R0001','name':'모험가라스'}, {'code':'HROCM_N3R0002','name':'아젤리아'}, {'code':'HROCM_N3R0003','name':'도살부대원'}, {'code':'HROCM_Y3R0003','name':'카오스교도살추적자'}, {'code':'HROCM_N3R0004','name':'카마인로즈'}, {'code':'HROCM_Y3R0004','name':'전도자카마인로즈'}, {'code':'HROCM_N3R0005','name':'캐롯'}, {'code':'HROCM_Y3R0005','name':'연구자캐롯'}, {'code':'HROCM_N3R0006','name':'헤이즐'}, {'code':'HROCM_Y3R0006','name':'마스코트헤이즐'}, {'code':'HROCM_N3R0007','name':'쥬디스'}, {'code':'HROCM_N3R0008','name':'네무나스'}, {'code':'HROCM_N3R0009','name':'디에리아'}, {'code':'HROCM_N3R0010','name':'갓마더'}, {'code':'HROCM_N3R0011','name':'자누타'}, {'code':'HROCM_N3R0012','name':'하탄'}, {'code':'HROCM_N3R0013','name':'멜라니'}
,{'code':'HROCM_N3B0001','name':'아이테르'}, {'code':'HROCM_N3B0002','name':'알렉사'}, {'code':'HROCM_N3B0003','name':'몽모랑시'}, {'code':'HROCM_Y3B0003','name':'수호천사몽모랑시'}, {'code':'HROCM_N3B0004','name':'바스크'}, {'code':'HROCM_N3B0005','name':'에노트'}, {'code':'HROCM_N3B0006','name':'헬렌'}, {'code':'HROCM_N3B0007','name':'이안'}, {'code':'HROCM_N3B0008','name':'제나'}, {'code':'HROCM_N3B0009','name':'레나'}, {'code':'HROCM_N3B0010','name':'미스티체인'}, {'code':'HROCM_N3B0011','name':'리마'}, {'code':'HROCM_Y3B0011','name':'뮤즈리마'}, {'code':'HROCM_N3B0012','name':'타라노르왕궁병사'}, {'code':'HROCM_N3B0013','name':'타라노르근위부대원'}, {'code':'HROCM_N3B0014','name':'무위'}
,{'code':'HROCM_N3G0001','name':'아딘'}, {'code':'HROCM_N3G0002','name':'아들라이'}, {'code':'HROCM_N3G0003','name':'에인즈'}, {'code':'HROCM_N3G0004','name':'크리스티'}, {'code':'HROCM_N3G0005','name':'펄호라이즌'}, {'code':'HROCM_Y3G0005','name':'인형제작가펄호라이즌'}, {'code':'HROCM_N3G0006','name':'쿠루리'}, {'code':'HROCM_Y3G0006','name':'매사냥꾼쿠루리'}, {'code':'HROCM_N3G0007','name':'글렌'}, {'code':'HROCM_N3G0008','name':'헬가'}, {'code':'HROCM_Y3G0008','name':'자유로운용병헬가'}, {'code':'HROCM_N3G0009','name':'제크토'}, {'code':'HROCM_N3G0010','name':'키리스'}, {'code':'HROCM_N3G0011','name':'루시'}, {'code':'HROCM_N3G0012','name':'무카차'}, {'code':'HROCM_N3G0013','name':'루지드'}, {'code':'HROCM_Y3G0013','name':'의적루지드'}, {'code':'HROCM_N3G0014','name':'오르테'}
,{'code':'HROCM_N4R0001','name':'아카테스'}, {'code':'HROCM_N4R0002','name':'코르부스'}, {'code':'HROCM_N4R0003','name':'딩고'}, {'code':'HROCM_N4R0004','name':'카와나'}, {'code':'HROCM_N4R0005','name':'카와주'}, {'code':'HROCM_N4R0006','name':'마야'}, {'code':'HROCM_N4R0007','name':'메르세데스'}, {'code':'HROCM_N4R0008','name':'슈리'}, {'code':'HROCM_N4R0009','name':'세릴라'}, {'code':'HROCM_N4R0010','name':'수린'}
,{'code':'HROCM_N4B0001','name':'안젤리카'}, {'code':'HROCM_N4B0002','name':'클라릿사'}, {'code':'HROCM_N4B0003','name':'콜리'}, {'code':'HROCM_N4B0004','name':'크로제'}, {'code':'HROCM_N4B0005','name':'도미니엘'}, {'code':'HROCM_N4B0006','name':'퓨리우스'}, {'code':'HROCM_N4B0007','name':'카린'}, {'code':'HROCM_N4B0008','name':'로만'}, {'code':'HROCM_N4B0009','name':'로제'}, {'code':'HROCM_N4B0010','name':'제라토'}
,{'code':'HROCM_N4G0001','name':'아밍'}, {'code':'HROCM_N4G0002','name':'카르투하'}, {'code':'HROCM_N4G0003','name':'시더'}, {'code':'HROCM_N4G0004','name':'레오'}, {'code':'HROCM_N4G0005','name':'랏츠'}, {'code':'HROCM_N4G0006','name':'퍼지스'}, {'code':'HROCM_N4G0007','name':'링'}, {'code':'HROCM_N4G0008','name':'실크'}
,{'code':'HROCB_N4R0001','name':'키즈나아이'}
,{'code':'HROCM_N5R0001','name':'아라민타'}, {'code':'HROCM_N5R0002','name':'바알세잔'}, {'code':'HROCM_N5R0003','name':'세실리아'}, {'code':'HROCM_N5R0004','name':'체르미아'}, {'code':'HROCM_N5R0005','name':'샬롯'}, {'code':'HROCM_N5R0006','name':'헤이스트'}, {'code':'HROCM_N5R0007','name':'화영'}, {'code':'HROCM_N5R0008','name':'일리나브'}, {'code':'HROCM_N5R0009','name':'카웨릭'}, {'code':'HROCM_N5R0010','name':'카일론'}, {'code':'HROCM_N5R0011','name':'켄'}, {'code':'HROCM_N5R0012','name':'리디카'}, {'code':'HROCM_N5R0013','name':'릴리아스'}, {'code':'HROCM_N5R0014','name':'멜리사'}, {'code':'HROCM_N5R0015','name':'폴리티스'}, {'code':'HROCM_N5R0016','name':'라비'}, {'code':'HROCM_N5R0017','name':'타마린느'}, {'code':'HROCM_N5R0018','name':'테네브리아'}, {'code':'HROCM_N5R0019','name':'폭격형카논'}
,{'code':'HROCM_N5B0001','name':'클로에'}, {'code':'HROCM_N5B0002','name':'슈'}, {'code':'HROCM_N5B0003','name':'에다'}, {'code':'HROCM_N5B0004','name':'엘레나'}, {'code':'HROCM_N5B0005','name':'플랑'}, {'code':'HROCM_N5B0006','name':'키세'}, {'code':'HROCM_N5B0007','name':'크라우'}, {'code':'HROCM_N5B0008','name':'루루카'}, {'code':'HROCM_N5B0009','name':'페이라'}, {'code':'HROCM_N5B0010','name':'란'}, {'code':'HROCM_N5B0011','name':'세즈'}, {'code':'HROCM_N5B0012','name':'세크레트'}, {'code':'HROCM_N5B0013','name':'타이윈'}, {'code':'HROCM_N5B0014','name':'유나'}, {'code':'HROCM_N5B0015','name':'제노'}
,{'code':'HROCM_N5G0001','name':'알렌시아'}, {'code':'HROCM_N5G0002','name':'바사르'}, {'code':'HROCM_N5G0003','name':'벨로나'}, {'code':'HROCM_N5G0004','name':'셀린'}, {'code':'HROCM_N5G0005','name':'찰스'}, {'code':'HROCM_N5G0006','name':'지휘형라이카'}, {'code':'HROCM_N5G0007','name':'데스티나'}, {'code':'HROCM_N5G0008','name':'에르발렌'}, {'code':'HROCM_N5G0009','name':'이세리아'}, {'code':'HROCM_N5G0010','name':'릴리벳'}, {'code':'HROCM_N5G0011','name':'루트비히'}, {'code':'HROCM_N5G0012','name':'모르트'}, {'code':'HROCM_N5G0013','name':'뮤이'}, {'code':'HROCM_N5G0014','name':'파벨'}, {'code':'HROCM_N5G0015','name':'레이'}, {'code':'HROCM_N5G0016','name':'로앤나'}, {'code':'HROCM_N5G0017','name':'세나'},{'code':'HROCM_N5G0018','name':'빌트레드'}, {'code':'HROCM_N5G0019','name':'비올레토'}, {'code':'HROCM_N5G0020','name':'비비안'}, {'code':'HROCM_N5G0021','name':'유피네'}, {'code':'HROCM_N5G0022','name':'자하크'}
,{'code':'HROLI_N5R0001','name':'바캉스유피네'}, {'code':'HROLI_N5R0002','name':'남국의이세리아'}, {'code':'HROLI_N5B0001','name':'세리스'}, {'code':'HROLI_N5B0002','name':'디에네'}, {'code':'HROLI_N5B0003','name':'메르헨테네브리아'}, {'code':'HROLI_N5B0004','name':'루나'}, {'code':'HROLI_N5B0005','name':'해변의벨로나'}, {'code':'HROLI_N5G0001','name':'랑디'}
,{'code':'HROCB_N5R0001','name':'솔'}, {'code':'HROCB_N5R0002','name':'엘페르트'}, {'code':'HROCB_N5B0003','name':'디지'}, {'code':'HROCB_N5G0004','name':'바이켄'}, {'code':'HROCB_N5B0005','name':'에밀리아'}, {'code':'HROCB_N5B0006','name':'렘'}, {'code':'HROCB_N5G0007','name':'람'}, {'code':'HROCB_N5R0008','name':'밀림'}, {'code':'HROCB_N5R0009','name':'슈나'}, {'code':'HROCB_N5G0010','name':'리무루'}
,{'code':'HROML_N3D0001','name':'아이노스'}, {'code':'HROML_N3D0002','name':'완다'}, {'code':'HROML_Y3D0002','name':'만능해결사완다'}, {'code':'HROML_N3D0003','name':'바터스'}, {'code':'HROML_N3D0004','name':'로리나'}, {'code':'HROML_Y3D0004','name':'지휘관로리나'}, {'code':'HROML_N3D0005','name':'휴라두'}, {'code':'HROML_N3D0006','name':'오틸리어'}, {'code':'HROML_N3D0007','name':'페넬로페'}, {'code':'HROML_N3D0008','name':'필리스'}, {'code':'HROML_Y3D0008','name':'흑기사필리스'}, {'code':'HROML_N3D0009','name':'레퀴엠로어'}, {'code':'HROML_N3D0010','name':'스벤'}, {'code':'HROML_N3D0011','name':'일리오스교도끼병'}, {'code':'HROML_Y3D0011','name':'카오스교도끼대장군'}, {'code':'HROML_N3D0012','name':'하솔'}
,{'code':'HROML_N3L0001','name':'아로웰'}, {'code':'HROML_N3L0002','name':'카밀라'}, {'code':'HROML_N3L0003','name':'리코리스'}, {'code':'HROML_Y3L0003','name':'선봉대장리코리스'}, {'code':'HROML_N3L0004','name':'셀레스트'}, {'code':'HROML_N3L0005','name':'도리스'}, {'code':'HROML_Y3L0005','name':'마법학자도리스'}, {'code':'HROML_N3L0006','name':'이튼'}, {'code':'HROML_N3L0007','name':'엘슨'}, {'code':'HROML_N3L0008','name':'글루미레인'}, {'code':'HROML_N3L0009','name':'군터'}, {'code':'HROML_N3L0010','name':'키키라트'}, {'code':'HROML_N3L0011','name':'미르사'}, {'code':'HROML_N3L0012','name':'소니아'}, {'code':'HROML_N3L0013','name':'윤령'}
,{'code':'HROML_N4D0001','name':'암살자카르투하'}, {'code':'HROML_N4D0002','name':'암살자시더'}, {'code':'HROML_N4D0003','name':'암살자콜리'}, {'code':'HROML_N4D0004','name':'보조형랏츠'}, {'code':'HROML_N4D0005','name':'배드캣아밍'}, {'code':'HROML_N4D0006','name':'혈검카린'}, {'code':'HROML_N4D0007','name':'외우주메르세데스'}, {'code':'HROML_N4D0008','name':'도전자도미니엘'}, {'code':'HROML_N4D0009','name':'승부의제라토'}, {'code':'HROML_N4D0010','name':'초승달무희링'}, {'code':'HROML_N4D0011','name':'대족장카와나'}, {'code':'HROML_N4D0012','name':'광염의카와주'}, {'code':'HROML_N4D0013','name':'고양이클라릿사'}, {'code':'HROML_N4D0014','name':'방랑용사레오'}, {'code':'HROML_N4D0015','name':'그림자로제'}, {'code':'HROML_N4D0016','name':'슈팅스타아카테스'}, {'code':'HROML_N4D0017','name':'죄악의안젤리카'},{'code':'HROML_N4D0018','name':'무법자크로제'}
,{'code':'HROML_N4L0001','name':'천사안젤리카'}, {'code':'HROML_N4L0002','name':'자애의로만'}, {'code':'HROML_N4L0003','name':'열화의딩고'}, {'code':'HROML_N4L0004','name':'홍염의아밍'}, {'code':'HROML_N4L0005','name':'전투형마야'}, {'code':'HROML_N4L0006','name':'여일의디에리아'}, {'code':'HROML_N4L0007','name':'대장퍼지스'}, {'code':'HROML_N4L0008','name':'구도자아이테르'}, {'code':'HROML_N4L0009','name':'풍운의수린'}, {'code':'HROML_N4L0010','name':'방랑자실크'}, {'code':'HROML_N4L0011','name':'주시자슈리'}
,{'code':'HROML_N5D0001','name':'화란의라비'}, {'code':'HROML_N5D0002','name':'집행관빌트레드'}, {'code':'HROML_N5D0003','name':'마신의그림자'}, {'code':'HROML_N5D0004','name':'적월의귀족헤이스트'}, {'code':'HROML_N5D0005','name':'잿빛숲의이세리아'}, {'code':'HROML_N5D0006','name':'종결자찰스'}, {'code':'HROML_N5D0007','name':'어둠의코르부스'}, {'code':'HROML_N5D0008','name':'디자이너릴리벳'}, {'code':'HROML_N5D0009','name':'나락의세실리아'}, {'code':'HROML_N5D0010','name':'무투가켄'}, {'code':'HROML_N5D0011','name':'조율자카웨릭'}, {'code':'HROML_N5D0012','name':'오퍼레이터세크레트'}, {'code':'HROML_N5D0013','name':'잔영의비올레토'}, {'code':'HROML_N5D0014','name':'환영의테네브리아'}, {'code':'HROML_N5D0015','name':'스트라제스'}, {'code':'HROML_N5D0016','name':'최강모델루루카'}
,{'code':'HROML_N5L0001','name':'야심가타이윈'}, {'code':'HROML_N5L0002','name':'벨리안'}, {'code':'HROML_N5L0003','name':'지배자릴리아스'}, {'code':'HROML_N5L0004','name':'사막의보석바사르'}, {'code':'HROML_N5L0005','name':'불신자리디카'}, {'code':'HROML_N5L0006','name':'심판자키세'}, {'code':'HROML_N5L0007','name':'라스트라이더크라우'}, {'code':'HROML_N5L0008','name':'사자왕체르미아'}, {'code':'HROML_N5L0009','name':'어린여왕샬롯'}, {'code':'HROML_N5L0010','name':'메이드클로에'}, {'code':'HROML_N5L0011','name':'빛의루엘'}, {'code':'HROML_N5L0012','name':'백은칼날의아라민타'}, {'code':'HROML_N5L0013','name':'현자바알세잔'}, {'code':'HROML_N5L0014','name':'설국의솔리타리아'}, {'code':'HROML_N5L0015','name':'실험체세즈'}, {'code':'HROML_N5L0016','name':'영안의셀린'} 
]

STD_COR = 0.5
STD_CHI = 100.0
STD_ITS = 0.2
STD_BHA = 0.8

STD_COR_B = 0.4
STD_ITS_B = 0.2
STD_BHA_B = 0.8

STD_COR_WL = 0.988
STD_CHI_WL = 4.0
STD_ITS_WL = 0.5
STD_BHA_WL = 0.5

def code_to_value(code, type):
    if type == 1: # code to hero
        for hero in hero_code.ALL_HEROS:
            if hero == code:
                return hero.toString()


def find_hero(image, part):
    value = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
    is_exist = False
    # part : L, R
    if part == 'L':
        for hero in ALL_HEROS:
            try: 
                url = 'crops/' + hero['code'] +'_L.jpg'
                src_img = cv2.imread(url)
                try:
                    url_ban = 'crops/' + hero['code'] +'_B_L.jpg'
                    src_img_ban = cv2.imread(url_ban)
                    if src_img_ban is None:
                        imgs = [image, src_img]
                    else:
                        is_exist = True
                        imgs = [image, src_img, src_img_ban]
                except:
                    imgs = [image, src_img]
                
                hists = []
                if src_img is not None:
                    for i, img in enumerate(imgs) :
                        plt.subplot(1,len(imgs),i+1)
                        plt.title('img%d'% (i+1))
                        plt.axis('off') 
                        plt.imshow(img[:,:,::-1])
                        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                        hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
                        cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
                        hists.append(hist)  

                    query = hists[0]
                    methods = {'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 'INTERSECT':cv2.HISTCMP_INTERSECT, 'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}
                    for j, (name, flag) in enumerate(methods.items()):
                        for i, (hist, img) in enumerate(zip(hists, imgs)):
                            #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
                            ret = cv2.compareHist(query, hist, flag)
                            if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
                                ret = ret/np.sum(query)        #비교대상으로 나누어 1로 정규화
                            value[i][j] = ret
                    if value[1][0] >= STD_COR and value[1][1] < STD_CHI and value[1][2] > STD_ITS and value[1][3] <= STD_BHA:
                        print(value)
                        return hero['name']
                    elif value[2][0] >= STD_COR_B and value[2][2] > STD_ITS_B and value[2][3] <= STD_BHA_B and is_exist == True:
                        print(value)
                        return hero['name']+':벤'
            except:
                pass
    elif part == 'R':
        for hero in ALL_HEROS:
            try: 
                url = 'crops/' + hero['code'] +'_R.jpg'
                src_img = cv2.imread(url)
                try:
                    url_ban = 'crops/' + hero['code'] +'_B_R.jpg'
                    src_img_ban = cv2.imread(url_ban)
                    if src_img_ban is None:
                        imgs = [image, src_img]
                    else:
                        is_exist = True
                        imgs = [image, src_img, src_img_ban]
                except:
                    imgs = [image, src_img]

                hists = []
                if src_img is not None:
                    for i, img in enumerate(imgs) :
                        plt.subplot(1,len(imgs),i+1)
                        plt.title('img%d'% (i+1))
                        plt.axis('off') 
                        plt.imshow(img[:,:,::-1])
                        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                        hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
                        cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
                        hists.append(hist)  

                    query = hists[0]
                    methods = {'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 'INTERSECT':cv2.HISTCMP_INTERSECT, 'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}
                    for j, (name, flag) in enumerate(methods.items()):
                        for i, (hist, img) in enumerate(zip(hists, imgs)):
                            #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
                            ret = cv2.compareHist(query, hist, flag)
                            if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
                                ret = ret/np.sum(query)        #비교대상으로 나누어 1로 정규화
                            value[i][j] = ret
                    if value[1][0] >= STD_COR and value[1][1] < STD_CHI and value[1][2] > STD_ITS and value[1][3] <= STD_BHA:
                        print(value)
                        return hero['name']
                    elif value[2][0] >= STD_COR_B and value[2][2] > STD_ITS_B and value[2][3] <= STD_BHA_B and is_exist == True:
                        print(value)
                        return hero['name']+':벤'
            except:
                pass
    elif part == 'FB':
        for hero in ALL_HEROS:
            try: 
                url = 'crops/' + hero['code'] +'_FB.jpg'
                src_img = cv2.imread(url)

                imgs = [image, src_img]

                hists = []
                if src_img is not None:
                    for i, img in enumerate(imgs) :
                        plt.subplot(1,len(imgs),i+1)
                        plt.title('img%d'% (i+1))
                        plt.axis('off') 
                        plt.imshow(img[:,:,::-1])
                        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                        hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
                        cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
                        hists.append(hist)  

                    query = hists[0]
                    methods = {'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 'INTERSECT':cv2.HISTCMP_INTERSECT, 'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}
                    for j, (name, flag) in enumerate(methods.items()):
                        for i, (hist, img) in enumerate(zip(hists, imgs)):
                            #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
                            ret = cv2.compareHist(query, hist, flag)
                            if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
                                ret = ret/np.sum(query)        #비교대상으로 나누어 1로 정규화
                            value[i][j] = ret
                    if value[1][0] >= STD_COR and value[1][1] < STD_CHI and value[1][2] > STD_ITS and value[1][3] <= STD_BHA:
                        print(value)
                        return hero['name']
            except:
                pass 
    elif part == 'WL':
        url = 'crops/RTN_WIN.jpg'
        url2 = 'crops/RTN_LOSE.jpg'
        src_img = cv2.imread(url)
        src_img2 = cv2.imread(url2)
        
        imgs = [image, src_img, src_img2]

        hists = []
        for i, img in enumerate(imgs) :
            plt.subplot(1,len(imgs),i+1)
            plt.title('img%d'% (i+1))
            plt.axis('off') 
            plt.imshow(img[:,:,::-1])
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
            cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
            hists.append(hist)  

        query = hists[0]
        methods = {'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 'INTERSECT':cv2.HISTCMP_INTERSECT, 'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}
        for j, (name, flag) in enumerate(methods.items()):
            for i, (hist, img) in enumerate(zip(hists, imgs)):
                            #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
                ret = cv2.compareHist(query, hist, flag)
                if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
                    ret = ret/np.sum(query)        #비교대상으로 나누어 1로 정규화
                value[i][j] = ret
            print('wl_value::',value)
            if value[1][0] >= STD_COR_WL and value[1][1] < STD_CHI_WL and value[1][2] > STD_ITS_WL and value[1][3] <= STD_BHA_WL:
                print(value)
                return '승리'
            elif value[2][0] >= STD_COR_WL and value[2][3] <= STD_BHA_WL:
                print(value)
                return '패배'
            else:
                print(value)
                return None
    else:
        return 'ERROR'