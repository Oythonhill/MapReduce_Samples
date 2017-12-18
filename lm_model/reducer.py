#!/usr/bin/anaconda2/bin/python
# @author: HongyuYin
# @email: hyhyin@163.com

import numpy as np
import sys

xtx_xty_total = np.zeros(20)

for line in sys.stdin:
    xtx_xty = line.split(",")
    xtx_xty = map(float,xtx_xty)
    xtx_xty_total = xtx_xty_total + xtx_xty


xtx = xtx_xty_total[0:16]
xtx.shape = (4,4)
xty = xtx_xty_total[16:20]
xty.shape = (4,1)


xtx_inverse = np.mat(xtx).I
B_hat = xtx_inverse.dot(xty)
print(B_hat)
