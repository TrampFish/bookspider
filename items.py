# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookspiderItem(scrapy.Item):
    book_title = scrapy.Field()
    book_author = scrapy.Field()
    book_img = scrapy.Field()
    book_price = scrapy.Field()
    book_press =scrapy.Field()
    book_publish_time = scrapy.Field()
    book_review_number = scrapy.Field()
