import sys, os
import numpy as np

class Memory_library:

    def __init__(self,size=200):
        self.s=[]
        self.a=[]
        self.r=[]
        self._s=[]
        self.size=size

    def in_put(self,s,a,r,_s):
        self.s.append(s)
        self.a.append(a)
        self.r.append(r)
        self._s.append(_s)

    
