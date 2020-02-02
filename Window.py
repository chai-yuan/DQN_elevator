import tkinter as tk

win = tk.Tk()
win.title('By CRI V0.0.4')
win.geometry('400x200')

# e = tk.Entry(win,show='#')
# e.pack()

txt = tk.Text(win,height=5,width=10)
txt.pack()

list_box = tk.Listbox(win,)

def insert():
    txt.insert("insert",)

button1 = tk.Button(win,text='print!!!'',command=insert)
button1.pack()
# button2 = tk.Button(win,text='working!!!',command=hit)
# button2.pack()

win.mainloop()