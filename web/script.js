eel.expose(print);
function print(content) {
	console.log(content);
}

eel.expose(set_page_title);
function set_page_title(title) {
	// alert(title);
	document.title = title + ' - Hexo Helper';
	document.getElementById("page-title").innerHTML = title;
}

eel.expose(set_content);
function set_content(content) {
	document.getElementById("content").innerHTML = content;
}

eel.expose(active_panel);
function active_panel() {
	panel = new mdui.Panel("#hexo-panel", {'accordion': true});
	panel.closeAll();
}

eel.expose(panelCloseAll);
function panelCloseAll() {
	panel.closeAll();
}

eel.expose(panelOpenAll);
function panelOpenAll() {
	panel.openAll();
}

async function init() {
	config = await eel.init()();
	hexo_path = config['hexo-path'];
	hexo_theme = config['hexo']['theme'];
	eel.load('home');
} init();