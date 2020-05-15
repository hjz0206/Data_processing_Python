#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/5/12 16:05
#@Author: Hou Jiazhen
#@File  : draw1_0.py

from matplotlib import pyplot as plt

#dpi参数可以让图片更加清晰
fig=plt.figure(figsize=(20,10),dpi=80)

x= range(2,26,2) #从2开始到26，步长为2
y= [15,13,14.5,17,20,25,26,26,24,22,18,15]

#绘制
plt.plot(x,y)
#设置x的刻度
#plt.xticks(x) 就可以和上面的步长2所对应
#range的第二个是取不到的！
_xticks_labels = [i/2 for i in range(4,49)]
#通过传一个列表可以取到0.5，plt.xticks(range(2,25,1))最后一个最小只能是1
plt.xticks(_xticks_labels[::3])


#保存图片
#plt.savefig("D:/Python/python3.8/sig_size.png")

plt.show()
