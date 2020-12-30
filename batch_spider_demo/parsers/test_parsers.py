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


class TestParsers(spider.BatchSpider):
    def start_requests(self, task):
        # task 为在任务表中取出的每一条任务
        id, url = task  # id， url为所取的字段，main函数中指定的
        yield spider.Request(url, task_id=id)

    def parser(self, request, response):
        title = response.xpath('//title/text()').extract_first()  # 取标题
        item = spider_test_item.SpiderTestItem()  # 声明一个item
        item.title = title  # 给item属性赋值
        yield item  # 返回item， item会自动批量入库
        yield self.update_task_batch(request.task_id, 1) # 更新任务状态为1

