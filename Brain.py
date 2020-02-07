# coding: utf-8
import sys, os
import numpy as np
import random
from Network import Network
import pandas as pd
import matplotlib.pyplot as plt

learning_rate = 0.05
greedy_rate = 0.8
eval_net = Network(input_size=11,hidden_size=10,output_size=3)
target_net = Network(input_size=11,hidden_size=10,output_size=3)

data = pd.read_excel("Memory_Library.xls")
size = data.shape[0]
check_num = 111

def put_data(s,a,r,_s):
    if(check_num>5):
        check_num=0
        pd.to_excel(data)
    
    r=np.array(r)
    data.loc[size] = np.concatenate((s,a[0],r,_s),axis=1)

def choice_action(s):
    print(s)
    return eval_net.predict(s[np.newaxis,:])

def learn(s,a,r,_s,batch):
    
    prediction = eval_net.predict(s)
    label = np.copy(prediction)
    target = target_net.predict(_s)
    list_target = target.tolist()

    print(label)
    print(prediction)

    for i in range(batch):
        label[i,int(a[i])]=r[i]+greedy_rate*max(list_target[i])
        print(label[i,int(a[i])])

    print('\n')
    print(prediction)
    print("差：\n")
    print(prediction-label)
    grad = eval_net.gradient(label,prediction)
    for key in ('W1', 'b1', 'W2', 'b2'):
        eval_net.params[key] += learning_rate * grad[key]

def learn_from_data(batch):
    num_data = np.array(data.sample(batch))
    s=num_data[:,0:11]
    a=num_data[:,11]
    r=num_data[:,12]
    _s=num_data[:,13:24]
    learn(s,a,r,_s,batch)

def trans_evl_to_target():
    target_net=eval_net

def draw_graph():
    x=np.linspace(0,len(eval_net._loss),len(eval_net._loss))
    y=eval_net._loss
    plt.plot(x,y)
    plt.show()



    