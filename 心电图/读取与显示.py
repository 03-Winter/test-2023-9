import matplotlib.pyplot as plt
import wfdb
import numpy as np
from sklearn.model_selection import train_test_split
# 设置测试集大小为20%的原始数据， 设置random_state可以保证每次执行训练时，拆分得到的训练集和测试集都相同， random_state 可以设置成任意整数，只要每次训练使用的值相同即可

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

datamax=3432
datamin=0

data=wfdb.rdrecord('100.dat', sampfrom=0, sampto=10000, physical=False, channels=[0, 1])
# record = ('data/MIT-BIH/100', sampfrom=0, sampto=10000, physical=False, channels=[0, 1])
plt.figure('heartrate')
plt.title(u'心电数据汇总')
plt.xlabel('time')
plt.ylabel('heatrate')
plt.xlabel(xmax=datamax,xmin=datamin)
plt.ylabel(ymax=150,ymin=0)
n=len(data)-1

train_test_split(data, test_size=0.2, random_state=42)


L1=plt.plot_date(data[:,0],data[:,1])
plt.axhline(y=60,color='g',linestyle='__')
plt.axhline(y=120,color='r',linestyle='__')
plt.legend([L1],['Joker'],loc='upper right')

plt.show()

