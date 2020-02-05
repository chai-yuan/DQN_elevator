from Brain import*
from Environment import*
import tkinter as tk

win = tk.Tk()
win.title('By CRI V0.3.3')
win.geometry('400x200')

def work_loop():
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


button1 = tk.Button(win,text="开始工作",command=work_loop)
button1.pack()

win.mainloop()
