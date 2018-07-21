import scrapy


class HelloSpider(scrapy.Spider):
    name = 'hello_spider'
    start_urls = ['http://www.cinearaujo.com.br/emcartaz.asp']

    # if you use 'start_urls', scrapy is gonna consider 'parse' as callback function
    def parse(self, response):
        self.log('Hello World')
        self.log(response.body)
