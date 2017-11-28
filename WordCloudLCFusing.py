# -*- coding: utf-8 -*-
from matplotlib import pyplot
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def chverWordc(ch_dist,save_p='',s_name=''):
    if save_p=='':
        save_p="D:/python_works/Python-s Exercise/ImageAndWordcloud-Class"
    if s_name=='':
        s_name="alicewordc.png"
    
    wordcloudc = WordCloud(font_path='C:\Windows\Fonts\simsun.ttc').\
                generate_from_frequencies(ch_dist)

    from os import path
    wordcloudc.to_file(path.join(save_p,s_name))
    print('ch finish')
    
def engverWordc(en_dist,save_p='',s_name=''):
    if save_p=='':
        save_p="D:/python_works/Python-s Exercise/ImageAndWordcloud-Class"
    if s_name=='':
        s_name="alicewordcEng.png"
    
    wordcloude = WordCloud(font_path='C:\Windows\Fonts\simsun.ttc').\
                generate_from_frequencies(en_dist)

    from os import path
    wordcloude.to_file(path.join(save_p,s_name))
    print('en finish')

def colorWordCould(e_dist):
    from PIL import Image
    import numpy as np
    bcimg=Image.open('D:/PS素材教程/漫威/mmexport148828636136611.png')
    bd=np.array(bcimg)
    wcld = WordCloud( background_color = 'white',    # 设置背景颜色
                mask = bd,
                max_words = 2000,            # 设置最大显示的字数
                max_font_size = 50,            # 设置字体最大值
                random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                )
    wordc=wcld.generate_from_frequencies(e_dist)
    ims=wordc.to_image()
    ims.show()

def showverwcloud(t_dist):
    wordcloud = WordCloud(font_path='C:\Windows\Fonts\simsun.ttc').\
                generate_from_frequencies(t_dist)

    ims=wordcloud.to_image()
    ims.show()

def cutTextver(vtxt):
    import jieba
    from collections import Counter
    #words=[]
    w_lst=jieba.lcut(vtxt)
    count=Counter(w_lst)
    w_resl = sorted(count.items(), key=lambda x: x[1], reverse=True)
    #w_resl  ==>list
    #print(type(count))
    return w_resl

def countToDist(ct_lst):#由list变成dist
    #ct_lst :  [(',', 9), (' ', 5), ('梅', 1)]
    filterW=[' ','.',',','。','，','!','&']
    w_dist={}
    for ilt in ct_lst:
        if ilt[0] in filterW:
            pass
        else:
            w_dist[ilt[0]]=ilt[1]
    
    return w_dist

    
def cutTextPath(txt_path): #限于中文
    if txt_path=='':
        return
    import jieba
    import re
    from collections import Counter
    words=[]
    with open(txt_path,'r',encoding='utf-8') as f:
        all_w=f.readlines()
        for w in all_w:
            if w!='':
                sk=jieba.lcut(w)
                patzer = re.compile(r'[\u4e00-\u9fa5]+')
                for i in sk:
                    pu=patzer.search(i)
                    if pu != None:
                        d=pu.group()
                        words.append(d)
    count=Counter(words)
    w_resl = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    #print(w_resl)
    return w_resl
    
def cutEngText(txt_path):
    if txt_path=='':
        return
    import jieba
    from collections import Counter
    words=[]
    with open(txt_path,'r',encoding='utf-8') as f:
        all_w=f.readlines()
        for w in all_w:
            if w!='':
                sk=jieba.lcut(w)
                for i in sk:
                    words.append(i)
    count=Counter(words)
    w_resl = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    #print(w_resl)
    return w_resl

def cretFreqDist():
    fq_d={}
    
    
    return fq_d

'''
生成词云图，保存词云图到文件，
允许词云图个性化。改变背景颜色，改字体，掩膜形状……
分词，生成词频字典。分词的进阶包括过滤特定词(stop word)，加入限定词

'''
'''
wc = WordCloud( background_color = 'white',    # 设置背景颜色
                mask = backgroud_Image,        # 设置背景图片 词云形状
                max_words = 2000,            # 设置最大显示的字数
                stopwords = STOPWORDS,        # 设置停用词，是从库中导入的
                font_path = 'C:/Users/Windows/fonts/msyh.ttf',# 设置字体，不设置显示不了中文
                max_font_size = 50,            # 设置字体最大值
                random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                )

mask传入的为ndarray格式，最好来自png，生成方式有：
## 1
from PIL import Image
import numpy as np
bdimg=np.array(Image.open(imgfile_path))
## 2
from scipy.misc import imread
alice_masking = imread(imgfile_path)
'''
if __name__ == '__main__':
    tdist={'天涯':26,'也有':38,'江南信':71,'梅破知春近':168,'少年心':55}
    s_path="D:/教学课件及学习资料/英语学习"
    s_name="1234567.png"
    text='虞美人,宜州见梅作,宋朝,黄庭坚,天涯也有江南信,梅破知春近 夜阑 风细 得香迟 不道晓来 开遍'\
    '向南枝,玉台弄粉花应妒,飘到眉心住,平生个里愿杯深,去国十年老尽少年心'
    #cutTextver(text)
    txt_path="D:/教学课件及学习资料/英语学习/TheAdventureoftheMysteriousStrangerEng.txt"
    wlst=cutEngText(txt_path)
    #wlst=cutTextPath(txt_path)
    w_frqu=countToDist(wlst)
    colorWordCould(w_frqu)
    #engverWordc(w_frqu,s_path,s_name='theAdvmy.png')
    #countToDist('')
    
    
    