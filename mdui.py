from functions import *
import re, json

def get(name):
	return read_partial(name)

def build(data):
	text = get(data['name'])
	for key, val in data.items():
		text = text.replace('{{ %s }}' % key, val)
	return text

def load(text):
	keys = re.findall(r'{%[\s\S]*?%}', text)
	# print('mdui.load()', text, keys)
	for key in keys:
		comd = ('{ %s }' % key[2:-2]).replace("'", '"').replace('\n', ' ').replace('\t', ' ')
		data = json.loads(comd)
		text = text.replace(key, build(data))
	return text