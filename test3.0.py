#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/5/15 10:41
#@Author: Hou Jiazhen
#@File  : test3.0.py 条形图练习

# noinspection PyUnresolvedReferences
from matplotlib import pyplot as plt
# noinspection PyUnresolvedReferences
import matplotlib
# noinspection PyUnresolvedReferences
from  matplotlib import font_manager

my_font = font_manager.FontProperties(fname="D:/CTEX/CTeX/fonts/truetype/chinese/simsun.ttf") #可以显示中文字体

plt.figure(figsize=(20,8),dpi=120)

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

x_14 = list(range(len(a)))
x_15 = [i+0.2 for i in x_14]
x_16 = [i+0.2*2 for i in x_14]

plt.xticks(x_15,a,fontproperties=my_font)

plt.bar(x_14,b_14,width=0.2,label="9月14日")
plt.bar(x_15,b_15,width=0.2,label="9月15日")
plt.bar(x_16,b_16,width=0.2,label="9月16日")

plt.legend(prop=my_font)

plt.grid(alpha=0.3)
plt.show()