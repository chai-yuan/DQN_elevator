import sys, os
import numpy as np
import pandas as pd

data = pd.read_excel("Memory_Library.xls")
size = data.shape[0]
check_num = 0

def get_batch(batch_size):
    num_data = np.array(data)
    row_rand_array = np.arange(num_data.shape[0])
    np.random.shuffle(row_rand_array)
    return array[row_rand_array[0:batch_size]]

def put_data(s,a,r,_s):
    if(check_num>5):
        check_num=0
        pd.to_excel(data)
    
    r=np.array(r)
    data.loc[size] = np.concatenate((s,a[0],r,_s),axis=1)

    
