import scrapy
from scrapy.selector import XmlXPathSelector
import re
import json
from datetime import datetime

def trimNumber(number):
	number = re.sub(r'\.(\d)k',r'\1 00', number)
	number = re.sub(r'comments',r'', number)
	number = re.sub(r'\s',r'', number)
	return number

def trimAuthor(author):
	author = re.sub(r'\w/',user, author)
	return author

def remExtras(text):
	text = re.sub(r'\t',r'\s', text)
	text = re.sub(r'\[[\s\w]+\]\s?',r'', text)
	text = re.sub(r'\s?\(.+\)\s?',r'', text)
	return text

class TSF(scrapy.Spider):
	name = "tsf"
	def start_requests(self):
		urls = [
			'http://feeds.tsf.pt/TSF-Destaques',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		response.selector.remove_namespaces()

		page = response.url.split("-")[-1]
		filename = "TSF-%s.json" % page

		myDict= []

		titles = response.xpath('//item/title/text()').extract()
		link = response.xpath('//item/link/text()').extract()
		description = response.xpath('//item/description/text()').extract()
		pubDate = response.xpath('//item/pubDate/text()').extract()
			
		for item in zip(titles,link,description,pubDate):
			myDict.append({
				'sentence': item[0],
				'link': item[1],
				'description': item[2],
				'pubDate': item[3]
			})

		data = datetime.now()

		newDict = {
			"date": str(data),
			"entries": myDict
		}
		with open(filename, 'w', encoding='utf8') as f:
			json.dump(newDict,f, ensure_ascii=False)
			self.log("Fechou ficheiro %s" % filename)
