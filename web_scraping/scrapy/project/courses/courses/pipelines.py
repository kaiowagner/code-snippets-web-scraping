# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class CoursesPipeline(object):
    def process_item(self, item, spider):
        self.conn.execute('insert into courses(title, url, image, description)'
                          ' values(:title, :url, :image, :description)', item)
        self.conn.commit()
        return item

    def create_table(self):
        result = self.conn.execute(" select name from sqlite_master"
                                   " where type='table' and name='courses' ")
        try:
            value = next(result)
        except StopIteration as ex:
            self.conn.execute('create table courses(id integer primary key, title text,'
                              ' url text, image text, description text)')

    def open_spider(self, spider):
        self.conn = sqlite3.connect('db.sqlite3')
        self.create_table()

    def close_spider(self, spider):
        self.conn.close()
