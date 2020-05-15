#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/5/12 16:05
#@Author: Hou Jiazhen
#@File  : draw1_0.py

from matplotlib import pyplot as plt
import random
# noinspection PyUnresolvedReferences
import matplotlib
from  matplotlib import font_manager

my_font = font_manager.FontProperties(fname="D:/CTEX/CTeX/fonts/truetype/chinese/simsun.ttf") #可以显示中文字体

#dpi参数可以让图片更加清晰
fig=plt.figure(figsize=(20,10),dpi=120)

x= range(0,120) #10到12点 x需要显示成字符串
y= [random.randint(20,35) for i in range(120)]

#绘制
plt.plot(x,y)
#设置x的刻度
#plt.xticks(x) 就可以和上面的步长2所对应
#range的第二个是取不到的！
_x = list(x)#只有list才可以用[::3]取步长

_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]
#通过传一个列表可以取到0.5，plt.xticks(range(2,25,1))最后一个最小只能是1
plt.xticks(_x[::3],_xticks_labels[::3],rotation=45,fontproperties=my_font)##前后数字和字符串一一对应，长度也要一样
#rotation 可以做旋转避免重合

##添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度(℃)",fontproperties=my_font)
plt.title("10点到12点每分钟的温度变化情况",fontproperties=my_font)

#保存图片
#plt.savefig("D:/Python/python3.8/sig_size.png")

plt.show()
