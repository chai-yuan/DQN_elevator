# coding: utf-8
import sys, os
import numpy as np
from Network import Network
from Memory import *

learning_rate = 0.1
greedy_rate = 0.8
eval_net = Network(input_size=11,hidden_size=10,output_size=3)
target_net = Network(input_size=11,hidden_size=10,output_size=3)

def choice_action(s):
    print(s)
    return eval_net.predict(s[np.newaxis,:])

def learn(s,a,r,_s):
    print(_s)
    _s=r+greedy_rate*_s   #待优化
    print(_s)
    _a = target_net.predict(_s[np.newaxis,:])
    grad = eval_net.gradient(a,_a)
    for key in ('W1', 'b1', 'W2', 'b2'):
        eval_net.params[key] += learning_rate * grad[key]
    
def learn_from_Memory(batch_size):
    batch_data = get_batch(batch_size)
    
    