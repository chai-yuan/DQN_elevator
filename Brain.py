# coding: utf-8
import sys, os
import numpy as np
from Network import Network
from Memory import Memory_library

memory_size = Memory_library(30)
learning_rate = 0.1
greedy_rate = 0.8
eval_net = Network(input_size=12,hidden_size=10,output_size=3)
target_net = Network(input_size=12,hidden_size=10,output_size=3)

def choice_action(s):
    return eval_net.predict(s[np.newaxis,:])

def learn(s,a,r,_s):
    _s=r+greedy_rate*_s   #待优化
    grad = network.gradient(s[np.newaxis,:],_s[np.newaxis,:]))
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] += learning_rate * grad[key]
    