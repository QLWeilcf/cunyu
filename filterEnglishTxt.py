# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:35:41 2017

@author: Ricardolcf
"""


def filterEnglishStr(ecMixTxt):
    #从复合文本中过滤出其中的英文句子
    #目前文本主要是中英混杂，不考虑单个词的情况
    engPat=re.compile(r'[A-Za-z]+.*')
    
    fec=open(ecMixTxt,'r',encoding='utf-8')
    line_fec=fec.readlines()
    save_eng_path="D:/教学课件及学习资料/英语学习/TheAdventureoftheMysteriousStrangerEng.txt"
    savetexteng=open(save_eng_path,'a+')
    for one_ln in line_fec:
        if one_ln !="":
            eng_sr=engPat.search(one_ln)
            if eng_sr!=None:
                savetexteng.write(eng_sr.group())
                savetexteng.write('\n')
                    
    print('end')
    
def filterChTxt(ecMixTxt):
    #从复合文本中过滤出其中的中文句子
    chPat=re.compile(r'[\u4e00-\u9fa5]+.*')
    fec=open(ecMixTxt,'r',encoding='utf-8')
    line_fec=fec.readlines()
    save_ch_path="D:/教学课件及学习资料/英语学习/TheAdventureofthezhong.txt"
    savetextch=open(save_ch_path,'a+')
    for one_ln in line_fec:
        if one_ln !="":
            ch_sr=chPat.search(one_ln)
            if ch_sr!=None:
                savetextch.write(ch_sr.group())
                savetextch.write('\n')
                    
    print('end ver')

if __name__ == '__main__':
    import re
    ecMixTxt="D:/教学课件及学习资料/英语学习/TheAdventureoftheMysteriousStranger.txt"
    
    filterEnglishStr(ecMixTxt)
    filterChTxt(ecMixTxt)