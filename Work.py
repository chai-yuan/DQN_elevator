from Brain import*
from Environment import*
import tkinter as tk

win = tk.Tk()
win.title('By CRI V0.3.4')
win.geometry('600x400')
e = tk.Entry(win)
e.pack()

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

def learn_memory():
    for i in range(int(e.get())):
        learn_from_data(2)

def trans_net():
    trans_evl_to_target()

button1 = tk.Button(win,text="开始工作",command=draw_graph)
button1.pack()
button2 = tk.Button(win,text="学习记忆",command=learn_memory)
button2.pack()
button3 = tk.Button(win,text="网络转置",command=trans_net)
button3.pack()

win.mainloop()
