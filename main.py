from tkinter import *
import tkinter.messagebox
import time
import os

hexo_path = '../oi'


window = Tk()
window.title('Hexo Helper (@memset0)')
window.minsize(320, 200)
window.maxsize(320, 200)

Label(window, text='当前时间').grid(row=0, column=0, padx=10, pady=4)
Label(window, text='文章名称').grid(row=1, column=0, padx=10, pady=4)

def getEntry():
    return

e = {}
v = {}
b = {}
list = ['time', 'post']

v['time'] = StringVar()
def refresh_time():
    v['time'].set(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    pass
e['time'] = Entry(window,
    borderwidth = 1,
    width = 25,
    textvariable = v['time'],
)
b['time'] = Button(window,
    text=' 刷新 ',
    command = refresh_time,
)

def new_post():
    os.system('cd {path} && hexo n {name} '.format(
        path = hexo_path,
        name = e['post'].get() or 'noname',
    ))
e['post'] = Entry(window,
    borderwidth=1,
    width=25,
)
b['post'] = Button(window,
    text=' 新建 ',
    command=new_post,
)

for it in range(0, len(list)):
    e[list[it]].grid(row = it, column = 1)
    b[list[it]].grid(row = it, column = 3, sticky = W, padx = 10, pady = 4)

refresh_time()

window.mainloop()

print('Bye!')
