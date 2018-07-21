# -*- coding: utf-8 -*-
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    allowed_domains = ['coursera.org']
    start_urls = ['http://coursera.org/']

    def parse(self, response):
        self.log('Hello World')
        self.log(response.body)
