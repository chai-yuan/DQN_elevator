# coding: utf-8
import sys, os
import numpy as np
from Network import Network
from Memory import Memory_library

memory_size = Memory_library(30)
learning_rate = 0.1
eval_net = Network(input_size=12,hidden_size=10,output_size=3)
target_net = Network(input_size=12,hidden_size=10,output_size=3)
