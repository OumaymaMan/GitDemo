
import scrapy
from ..items import QuotetutorialItem
 
class voiture_propre(scrapy.Spider) :
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
 
    def parse(self, response) :
 
        items = QuotetutorialItem()
 
        all_div_quotes = response.css('div.quote')
 
        for quotes in all_div_quotes:
 
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
 
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
 #$x('/html/body/div/p[2]/a')
            #/html/body/div[1]/div/main/div/div[7]/div/div[4]/div[1]/div/div[2]/div[1]/div[2]
            #//*[@id="main-content"]/div/div[7]/div/div[4]/div[1]/div/div[2]/div[1]/div[2]


            yield items