# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bookspider.items import  BookspiderItem
from pymongo import MongoClient

#使用MongoDB数据库存储当当网中的图书数据
client = MongoClient()
collection = client["book"]["dangdang"]

class BookspiderPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,BookspiderItem):
            collection.insert(dict(item))
            print(item)


