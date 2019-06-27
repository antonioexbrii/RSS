import scrapy
from scrapy.selector import XmlXPathSelector
import re
import json
from datetime import datetime

def filter(text):
	text = text.lower()
	text = re.sub(r'[\'\"]','',text)
	text = re.sub(r'[.!?:;,]','',text)
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
				'sentence': filter(item[0]),
				'title': item[0],
				'link': item[1],
				'desc_sentence': filter(item[2]),
				'descricao': item[2],
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
