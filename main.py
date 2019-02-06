from functions import *
import eel, os, re, yaml, json
import mdui

eel.init('web')

@eel.expose
def open_file(path):
	os.system(config['command']['open-file'].format(path=path))

@eel.expose
def open_folder(path):
	os.system(config['command']['open-folder'].format(path=path))

@eel.expose
def load(name):
	if name == 'home':
		eel.set_page_title('主页')
		eel.set_content(mdui.load(mdui.get('home/body')))
	elif name == 'post':
		eel.set_page_title('文章管理')

@eel.expose
def init():
	global config
	config = yaml.load(read_file('config.yml'))
	config['hexo'] = yaml.load(read_file(config['hexo-path'] + '_config.yml'))
	return config

eel.start('index.html', size=(1200,800))