from functions import *
import mdui, hexo
import eel, sys, os, re, yaml, json

envi_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
os.chdir(envi_path)

eel.init('web')

@eel.expose
def open_file(path):
	os.system(config['command']['open-file'].format(path=path))

@eel.expose
def open_folder(path):
	os.system(config['command']['open-folder'].format(path=path))

@eel.expose
def open_post(name):
	open_file(hexo_path + '/source/_posts/' + name)

class Post:
	def get(self, key):
		if not key in self.config.keys():
			return ''
		elif self.config[key] == None:
			return ''
		elif type(self.config[key]) == list:
			if len(self.config[key]) == 0:
				return ''
			answer = self.config[key][0]
			for i in range(1, len(self.config[key])):
				answer += ', ' + self.config[key][i]
			return answer
		else:
			return self.config[key]
	def __init__(self, filename):
		text = read_file(hexo_path + '/source/_posts/' + filename)
		self.text = text
		self.config_text = '{}'
		for temp in text.split('---'):
			if re.sub(r'[ \n]*', '', temp) != '':
				self.config_text = temp
				break
		self.config = yaml.load(self.config_text)
		self.tags       = self.get('tags')
		self.date       = str(self.config['date'])
		self.title      = self.config['title']
		self.filename   = filename
		self.categories = self.get('categories')

@eel.expose
def load(name):
	if name == 'home':
		eel.set_page_title('主页')
		eel.set_content(mdui.load(mdui.get('home/body')))
	elif name == 'post':
		eel.set_page_title('文章管理')
		posts = []
		post_name_list = os.listdir(hexo_path + '/source/_posts')
		for post_name in post_name_list:
			path = hexo_path + '/source/_posts/' + post_name
			if os.path.splitext(path)[-1] == '.md':
				posts.append(Post(post_name))
		content = ''
		posts.sort(key=lambda x: x.date, reverse=True)
		for post in posts:
			content += mdui.build({
				'name'      : 'post/item',
				'date'      : post.date,
				'tags'      : post.tags,
				'title'     : post.title,
				'filename'  : post.filename,
				'categories': post.categories,
			})
		eel.set_content(mdui.get('post/panel').replace('{{ content }}', content))
		eel.active_panel()

@eel.expose
def init():
	global config, hexo_path
	config = yaml.load(read_file(os.getcwd() + '/config.yml'))
	config['hexo'] = yaml.load(read_file(config['hexo-path'] + '_config.yml'))
	hexo_path = os.path.abspath(config['hexo-path'])
	return config

eel.start('index.html', size=(1200,800))