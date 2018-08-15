from tkinter import *
import tkinter.messagebox
import time
import os

hexo_path = 'C:\\Users\\surface\\Desktop\\Hexo\\oi'

window = Tk()
window.title('Hexo Helper (@memset0)')
window.minsize(320, 160)
window.maxsize(320, 160)

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
    os.system('cd {path} && hexo n "{name}"'.format(
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
row = [0, 0, 0, 0, 1, 1, 1, 1]
column = [0, 1, 2, 3, 0, 1, 2, 3]
list = ['hexo_s', 'hexo_clean','hexo_g', 'hexo_d', 'open_dir', 'open_post', 'open_theme', 'open_public']

# [一键命令] 一键完成 ... 操作

def hexo_s():
    os.system('start "Hexo 正在调试（请勿关闭本窗口）" /min cmd /c "cd {path} && hexo s"'.format(path = hexo_path))
b['hexo_s'] = Button(Frame2, text=' 一键调试 ', command = hexo_s)

def hexo_clean():
    os.system('start "Hexo 正在清理提交目录" /min cmd /c "cd {path} && hexo clean"'.format(path = hexo_path))
b['hexo_clean'] = Button(Frame2, text=' 一键清理 ', command = hexo_clean)

def hexo_g():
    os.system('start "Hexo 正在生成静态博客文件" /min cmd /c "cd {path} && hexo g"'.format(path = hexo_path))
b['hexo_g'] = Button(Frame2, text=' 一键生成 ', command = hexo_g)

def hexo_d():
    os.system('start "Hexo 正在生成并提交提交静态博客文件" /min cmd /c "cd {path} && hexo d -g"'.format(path = hexo_path))
b['hexo_d'] = Button(Frame2, text=' 一键提交 ', command = hexo_d)

# [打开目录] 一键打开 ... 目录

def open_dir():
    os.system('explorer "{path}"'.format(path = hexo_path))
b['open_dir'] = Button(Frame2, text=' 打开目录 ', command = open_dir)

def open_post():
    os.system('explorer "{path}\\source\\_posts"'.format(path = hexo_path))
b['open_post'] = Button(Frame2, text=' 打开文章 ', command = open_post)

def open_theme():
    os.system('explorer "{path}\\themes"'.format(path = hexo_path))
b['open_theme'] = Button(Frame2, text=' 打开主题 ', command = open_theme)

def open_public():
    os.system('explorer "{path}\\public"'.format(path = hexo_path))
b['open_public'] = Button(Frame2, text=' 打开结果 ', command = open_public)


for it in range(0, len(list)):
    # print(it, list[it], row[it], column[it])
    b[list[it]].grid(row = row[it], column = column[it], sticky = W, padx = 5, pady = 4)

refresh_time()
window.mainloop()

print('Bye!')
