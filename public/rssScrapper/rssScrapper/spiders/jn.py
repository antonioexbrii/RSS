import scrapy
from scrapy.selector import XmlXPathSelector
import re
import json
from datetime import datetime

i=0

def filter(text):
  text = text.lower()
  text = re.sub(r'[\'\"]','',text)
  text = re.sub(r'[.!?:;,]','',text)
  return text
	
class JN(scrapy.Spider):
  name = "jn"
  def start_requests(self):
    urls = [
        'http://feeds.jn.pt/JN-Justica',
        'http://feeds.jn.pt/JN-Gente',
        'http://feeds.jn.pt/JN-Nacional',
        'http://feeds.jn.pt/JN-Mundo',
        'http://feeds.jn.pt/JN-Economia',
        'http://feeds.jn.pt/JN-Pais',
        'http://feeds.jn.pt/JN-Desporto',
  ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    response.selector.remove_namespaces()
    global i
    filename='../data/jn'+str(i)+'.json'
    i += 1
    myDict=[]

    title = response.xpath('//item/title/text()').extract()
    link = response.xpath('//item/link/text()').extract()
    description = response.xpath('//item/description/text()').extract()
    pubDate = response.xpath('//item/pubDate/text()').extract()
    for item in zip(title,link,description,pubDate,):
      myDict.append({
        'sentence': filter(item[0]),
        'title': item[0],
        'link': item[1],
        'description': item[2],
        'pubDate': item[3],
      })

    data = datetime.now()

    newDict = {
      "date": str(data),
      "entries": myDict
    }
    with open(filename, 'w', encoding='utf8') as f:
      json.dump(newDict,f, ensure_ascii=False)
      self.log('Fechou ficheiro %s' % filename)
      