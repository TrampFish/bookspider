# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from bookspider.items import BookspiderItem


class DangdangSpider(RedisCrawlSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    redis_key = "dangdang"

    # start_urls = ['http://dangdang.com/']

    rules = (
        #图书的大分类以及小分类
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='con flq_body']/div//dd/a",)), follow=True),
        #获取图书的详细页URL
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='search_nature_rg']/ul/li/a",)),callback="parse_detail"),
        #获取图书列表页的下一页URL
        Rule(LinkExtractor(restrict_xpaths=("//a[@title='下一页']/@href",)),follow=True)
    )

    def parse_detail(self,response):
        item =  BookspiderItem()
        item["book_title"] = response.xpath("//div[@class='name_info']/h1/@title").extract_first()
        item["book_img"] = response.xpath("//div[@id='largePicDiv']/a/img/@src").extract_first()
        item["book_price"] = response.xpath("//p[@id='dd-price']/text()[2]").extract_first()
        item["book_author"] = response.xpath("//span[@id='author']/text()|//span[@id='author']/a/text()").extract()
        item["book_press"] = response.xpath("//span[@dd_name='出版社']/a/text()").extract_first()
        item["book_publish_time"] = response.xpath("//div[@class='messbox_info']/span[3]/text()").extract_first()
        item["book_review_number"] = response.xpath("//span[@class='star_box']/../a/text()").extract_first()
        #难点：图书详细页返回的响应中没有图书简介和作者简介，不知道通过什么方式生成在浏览器上的，在Network下未找到包含相同内容的文件，下一步通过selenium获取图书简介和作者简介
        #同时想到另外一种解决思路，构造作者以及图书的的百度搜索URL请求，获取百度上的简介
        yield item
