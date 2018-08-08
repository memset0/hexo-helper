from tkinter import *
import tkinter.messagebox
import time
import os

hexo_path = 'C:\\Users\\surface\\Desktop\\Hexo\\oi'

window = Tk()
window.title('Hexo Helper (@memset0)')
window.minsize(320, 200)
window.maxsize(320, 200)

Frame1 = Frame(window)
Frame1.pack()
Frame2 = Frame(window)
Frame2.pack()

l = {}
e = {}
v = {}
b = {}
list = ['time', 'new_post']

# ===== 第一部分 =====

# [当前时间] 获取当前时间并提供复制功能
v['time'] = StringVar()
def refresh_time():
    v['time'].set(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
l['time'] = Label(Frame1, text='当前时间')
b['time'] = Button(Frame1, text=' 刷新 ', command = refresh_time)
e['time'] = Entry(Frame1,
    width = 25,
    textvariable = v['time'],
)

# [新建文章] 根据 Hexo Path 来新建文章
def new_post():
    os.system('cd {path} && hexo n {name} '.format(
        path = hexo_path,
        name = e['new_post'].get() or 'noname',
    ))
l['new_post'] = Label(Frame1, text='文章名称')
b['new_post'] = Button(Frame1, text=' 新建 ', command=new_post)
e['new_post'] = Entry(Frame1,
    borderwidth=1,
    width=25,
)

# 固定第一部分固件
for it in range(0, len(list)):
    l[list[it]].grid(row = it, column=0, padx=10, pady=4)
    e[list[it]].grid(row = it, column = 1)
    b[list[it]].grid(row = it, column = 2, sticky = W, padx = 10, pady = 4)

# ===== 第二部分 =====

b = {}
list = ['server', 'open_dir', 'open_post']

# [启动调试] 开启 Hexo Server

def start_server():
    os.system('start cmd /c "cd {path} && hexo s"'.format(
        path = hexo_path,
    ))
b['server'] = Button(Frame2, text=' 开启调试 ', command = start_server)

def open_dir():
    os.system('explorer "{path}"'.format(path = hexo_path))
b['open_dir'] = Button(Frame2, text=' 打开目录 ', command = open_dir)

def open_post():
    os.system('explorer "{path}\\source\\_posts"'.format(path = hexo_path))
b['open_post'] = Button(Frame2, text=' 打开文章目录 ', command = open_post)


for it in range(0, len(list)):
    b[list[it]].grid(row = 0, column = it, sticky = W, padx = 10, pady = 4)

refresh_time()
window.mainloop()

print('Bye!')