# coding: utf-8
import sys, os
import numpy as np
from charain_train_network import train_network

#创建网络
network = train_network(input_size=10, hidden_size=6, output_size=3)
learning_rate = 0.1

#动作
work3 = 0
work2 = 0
work = 2

#读取文件
try:
    f = open('./file.txt', 'r')
    for lines in f.readlines():#读取每一行
        number=[]
        lines=lines.split(' ')#将字符串分割成列表
        for line in lines:
            if(line!='\n'):number.append(float(line))#忽略换行符
        number.append(float(work))
        number.append(float(work2))
        number.append(float(work3))
        work3=work2
        work2=work
        print(number)
        x=np.array(number)#转换为矩阵
        print(x)
        y=network.predict(x[np.newaxis,:])#增加一个维度（为了用上之前写的批处理库）
        print(y)
        work = np.argmax(y[0])
        if(work==0):print("UP!!!")
        elif(work==1):print("DOWN!!!")
        else:print("DO NOT MOVE!!!")

finally:
    if f:
        f.close()
    else:
        print("Error!!!")