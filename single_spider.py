# -*- coding: utf-8 -*-
'''
Created on 2020-12-30 15:13:59
---------
@summary:
---------
@author: liubo
'''

import spider


class SingleSpider(spider.SingleSpider):
    def start_requests(self, *args, **kws):
        yield spider.Request("https://www.baidu.com")

    def parser(self, request, response):
        # print(response.text)
        print(response.xpath('//input[@type="submit"]/@value').extract_first())


if __name__ == "__main__":
    SingleSpider().start()