#!/usr/bin/anaconda2/bin/python
# @author: HongyuYin
# @email: hyhyin@163.com

import sys
import numpy as np

# calc xty and xtx
xx = np.zeros(16)
xy = np.zeros(4)
temp = []
for line in sys.stdin:
    temp = []
    line = line.strip().split(",")
    line[1:1] = [1]
    line = np.array(map(float,line))
    xy = xy + line[0]*line[1:len(line)]

    x = line[1:len(line)]
    for j in range(0,len(x)):
        for k in range(0,len(x)):
            temp.append(x[j]*x[k])
    xx = xx + np.array(temp)

xy = xy.tolist()
xx = xx.tolist()
xy[0:0] = xx
xy = map(str,xy)
xx_xy = ",".join(xy)

print xx_xy
