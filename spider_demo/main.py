# -*- coding: utf-8 -*-
"""
Created on 2020-07-12 22:25:43
---------
@summary: 爬虫入口
---------
@author: liubo
"""

from parsers import *

if __name__ == "__main__":
    spider = test_parsers.TestParsers(table_folder="test:test1")
    spider.start()
