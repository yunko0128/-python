#coding:utf-8
#!/usr/bin/env python

from xml.etree.ElementTree import ElementTree
from urllib import urlopen

def parse_rss(url):
	#rss2.0をパースして、辞書のリストを返す
	rss = ElementTree(file=urlopen(url))
	root = rss.getroot()
	rsslist = []
	
	#rss2.0のitemだけ抜き出す
	for item in [x for x in root.getiterator() if "item" in x.tag]:
		rssdict = {}
		for elem in item.getiterator():
			for k in ['link','title','description','author','pubDate']:
				if k in elem.tag:
					rssdick[k] = elem.text
				else:
					rssdick[k] = rssdick.get(k,"N/A")
			rsslist.append(rssdick)
	return rsslist

