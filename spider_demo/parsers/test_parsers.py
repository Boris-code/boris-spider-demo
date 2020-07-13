# -*- coding: utf-8 -*-
'''
Created on 2020-07-12 22:29:31
---------
@summary:
---------
@author: liubo
'''

import spider
from items import *


class TestParsers(spider.Spider):
    def start_requests(self, *args, **kws):
        yield spider.Request("https://www.baidu.com")

    def parser(self, request, response):
        title = response.xpath('//title/text()').extract_first()  # 取标题
        item = spider_test_item.SpiderTestItem()  # 声明一个item
        item.title = title  # 给item属性赋值
        yield item  # 返回item， item会自动批量入库

