import os
import urllib
import urllib2

#"C:\\Program Files\\Python2.7\\python.exe"

def download_images(A,B):
	for i in range(A,B):
		url = "http://comicjk.com/Pics/Comic%d.gif" % i
		message = urllib.urlretrieve(url, os.path.basename(url))[1]
		#for x in message.__dict__:
		#	print x, message.__dict__[x]
		if message.type != 'image/gif':
			url = "http://comicjk.com/Pics/Comic%d.png" % i
			message = urllib.urlretrieve(url, os.path.basename(url))[1]
			if message.type != 'image/png': break
			
def remove_unused_gifs():
	f = open('is_png.txt', 'w')
	for i in range(0,939):
		if os.path.isfile('Comic%d.png' % i):
			f.write('1')
			os.remove('Comic%d.gif' % i)
		else:
			f.write('0')

def rename_Comic():
	for i in range(0,939):
		if os.path.isfile('Comic%d.gif' % i):
			os.rename('Comic%d.gif' % i, '%d.gif' % i)
		if os.path.isfile('Comic%d.png' % i):
			os.rename('Comic%d.png' % i, '%d.png' % i)

def get_text():
	hover = open('hovertext.txt', 'w')
	titles = open('titles.txt', 'w')
	for i in range(0,939):
		url = "http://comicjk.com/comic.php/%d" % i
		content = urllib2.urlopen(url).read()
		
		start = content.find('title="') + len('title="')
		end = content.find('"', start)
		while content[end-1]=='\\':
			end = content.find('"', end+1)
		hover.write(content[start:end]+'\n')
		
		start = content.find('<title>') + len('<title>')
		end = content.find('</title>', start)
		titles.write(content[start:end]+'\n')

def download_html(A,B):
	for i in range(A,B):
		url = "http://comicjk.com/comic.php/%d" % i
		urllib.urlretrieve(url, os.path.join('html', '%d.html' % i))

download_html(0,939)
