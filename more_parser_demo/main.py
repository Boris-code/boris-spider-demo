# -*- coding: utf-8 -*-
"""
Created on 2020-07-12 22:25:43
---------
@summary: 爬虫入口
---------
@author: liubo
"""

from spider import Spider

from parsers import *

if __name__ == "__main__":
    spider = Spider(table_folder="test:more_parser")
    spider.add_parser(baidu_parser.BaiduParser)
    spider.add_parser(bing_parser.BingParser)
    spider.start()
