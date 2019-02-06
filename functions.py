def partial_path(name):
	return 'web/partial/{name}.html'.format(name=name)

def read_file(path):
	file = open(path, 'r+', encoding='utf8')
	text = file.read()
	file.close()
	return text

def read_partial(name):
	return read_file(partial_path(name))