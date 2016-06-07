import urllib.request
import xml.etree.ElementTree
from datetime import date
from datetime import datetime
import time
import sched

def retrieve():
	html = urllib.request.urlopen('https://www.bing.com/news?format=RSS').read()
	root = xml.etree.ElementTree.fromstring(html)
	today = date.today()
	name = date(today.year, today.month, today.day).isoformat() + '.txt'
	file = open(name, 'w')
	try:
#		file.write('retrieved at ' + date(today.year, today.month, today.day).ctime() + '\n')
		file.write('retrieved at ' + str(datetime.utcnow()) + '\n')
		for item in root.find('channel').findall('item'):
			file.write(item.find('title').text + '\n')
	except:
		file.close()
	file.close()
	print("HE")
	
def process():
	retrieve()
	s.enter(daily, 1, process, ())

def main():
	process()
	s.run()

if __name__ == '__main__':
	daily = 60*60*24
	s = sched.scheduler(time.time, time.sleep)
	main()
