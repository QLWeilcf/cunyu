#coding=utf-8
def readgisone():#对e00文件进行预处理
    import re
    sfile="D:***.e00"
    savef="D:\***\chinahadre.txt"
    lsd=[]
    fi=open(savef,'a+')
    with open(sfile,'r') as f:
        ls=f.readlines()
    
    #patz=re.compile(r'E\+')
    for i in ls:
        if 'E+' in i:
            k=i.split()#字符串列表
            
#for e00 to raster file 
readgisone()
