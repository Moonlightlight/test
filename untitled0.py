# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:42:21 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
fracs = [5,4,4,4,4]
labels = 'xiwang', 'daima', 'biancheng','meiyou','xingqu'
explode = [ 0.1,0,0,0,0] 
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
plt.show()