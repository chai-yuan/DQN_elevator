from Brain import*
from Environment import*
import tkinter as tk

win = tk.Tk()
win.title('By CRI V0.3.2')
win.geometry('400x200')


for episode in range(10):

    state,reward =IO_Environment().get_environment()

    while True:
        #选择当前动作
        action = choice_action(state)
        #执行动作
        IO_Environment().put_out_action(action)
        #获得改变后环境与奖励
        _state,reward = IO_Environment().get_environment()
        #学习或者储存
        learn(state,action,reward,_state)
        #环境交替
        state=_state

