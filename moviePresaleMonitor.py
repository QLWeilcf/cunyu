import time 
import requests
import traceback
from wxpy import *
from lxml import etree
import tkinter as tk
from tkinter import messagebox

def getOneUrl(url):
    try:
        r=requests.get(url,timeout=30)
        #r.encoding=r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()
        return None

def showMsg():
    window = tk.Tk()
    window.title('prrrrrr')
    window.geometry('400x400')
    tk.Button(window,text='presale').pack()
    window.mainloop()

def showMsg2():
    win = tk.Tk()
    win.title('prrrrrr')
    win.geometry('400x400')
    tk.Button(win,text='presale').pack()
    win.mainloop()

def monitorBtnbuy(url,t=0):
    bot = Bot()
    while True:
        txt=getOneUrl(url)
        if txt==None:
            #time.sleep(2)
            pass
        else: 
            html=etree.HTML(txt)
            try:
                ptxt=html.xpath('/html/body/div[3]/div/div[2]/div[2]/a/text()')
                if ptxt==[]:
                    if t%5==0:
                        print('现在是{0},还没有预售信息；t={1}'.format(time.asctime(),t))
                        time.sleep(180)
                    if t%2==0:
                        time.sleep(15*60) #15分钟
                    time.sleep(120)
                elif ptxt[0]=='特惠购票': #赶紧想办法提醒自己
                    print(time.asctime(),ptxt[0])
                    group = bot.groups().search('def-self')[0] #给特定的群里发消息
                    group.send('预售开始！')
                    group.send(url)
                    print('msg.send()')
                    showMsg()
                    showMsg2()
            except:
                traceback.print_exc()
        time.sleep(5)
        t+=1
        #if t>20:break


url1='https://maoyan.com/films/1156894'
url='https://maoyan.com/films/248172' #Avengers: Endgame
monitorBtnbuy(url,t=0)




