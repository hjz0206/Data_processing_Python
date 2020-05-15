#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/5/12 21:54
#@Author: Hou Jiazhen
#@File  : test2.py

from matplotlib import pyplot as plt
import random
# noinspection PyUnresolvedReferences
import matplotlib
from  matplotlib import font_manager

my_font = font_manager.FontProperties(fname="D:/CTEX/CTeX/fonts/truetype/chinese/simsun.ttf") #可以显示中文字体

#dpi参数可以让图片更加清晰
fig=plt.figure(figsize=(15,10),dpi=120)

x= range(0,9)
y1= [0.07847,0.0567,0.03715,0.02211,0.01234,0.00619,0.00239,0.00096,0.00024]
y2= [0.077895,0.057035,0.037845,0.022525,0.012225,0.00586,0.002575,0.00079,0.000225]
y3=[0.14062,0.1199,0.097177,0.077632,0.058757,0.042333,0.027735,0.016495,0.00928]
y4=[0.19948,0.17742,0.15679,0.13663,0.11826,0.10069,0.083548,0.067438,0.05222]

#绘制两条线
plt.plot(x,y1,label="BPSK",color="red",linewidth=2)
plt.plot(x,y2,label="QPSK",color="yellow",linewidth=2)
plt.plot(x,y3,label="16-QAM",color="blue",linewidth=2)
plt.plot(x,y4,label="64-QAM",color="purple",linewidth=2)

#设置x的刻度
#_xticks_labels = ["{}岁".format(i) for i in x]
#plt.xticks(x,_xticks_labels,fontproperties=my_font)

##绘制网格
plt.grid(alpha=0.4)##alpha设置透明度
##如果觉得网格稀疏不合适应该去调整xticks/yticks

##绘制图例
plt.legend(prop=my_font,loc="0")##这里添加中文比较特殊

##添加描述信息
plt.xlabel("Eb/n0")
plt.ylabel("ber")
plt.title("数字基带调制解调四种调制方式比较",fontproperties=my_font)

#保存图片
plt.savefig("D:/Python/python3.8/1.png")

plt.show()