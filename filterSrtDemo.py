# -*- coding: utf-8 -*-


def filterEngSrt(ecMixTxt):
    #从字幕中过滤掉其中的中文句子
    #目前文本主要是中英混杂，不考虑单个词的情况
    #engPat=re.compile(r'[A-Za-z]+.*')
    chPat=re.compile(r'[\u4e00-\u9fa5]+.*')
    fec=open(ecMixTxt,'r',encoding='utf-8')
    line_fec=fec.readlines()
    save_eng_path="D:/BaiduYunDownload/黑镜s3e2/S04E01eng.srt"
    savetexteng=open(save_eng_path,'a+',encoding='utf-8')
    for one_ln in line_fec:
        if one_ln !="":
            ch_sr=chPat.search(one_ln)
            if ch_sr!=None:
                pass
            else:
                savetexteng.write(one_ln)
                #savetextch.write('\n')
        else:
            savetexteng.write('\n')

   
    print('end')
	
ecMixTxt="D:/BaiduYunDownload/黑镜s3e2/S04E01.srt"
filterEngSrt(ecMixTxt)