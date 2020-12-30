# -*- coding: utf-8 -*-
"""
Created on 2020-07-12 22:25:43
---------
@summary: 爬虫入口
---------
@author: liubo
"""

from parsers import *
from spider import ArgumentParser


def crawl_test(args):
    spider = test_parsers.TestParsers(
        task_table="batch_spider_task",  # mysql中的任务表
        batch_record_table="batch_spider_batch_record",  # mysql中的批次记录表
        batch_name="批次爬虫测试(周全)",  # 批次名字
        batch_interval=7,  # 批次时间 天为单位 若为小时 可写 1 / 24
        task_keys=["id", "url"],  # 需要获取任务表里的字段名，可添加多个
        table_folder="test:batch_spider",  # redis中存放request等信息的根key
        task_state="state",  # mysql中任务状态字段
    )

    if args == 1:
        spider.start_monitor_task()  # 监控与下发任务

    if args == 2:
        spider.start()  # 采集


if __name__ == "__main__":
    parser = ArgumentParser(description="批次爬虫示例")
    parser.add_argument(
        "--crawl_test", type=int, nargs=1, help="批次爬虫测试(1|2）", function=crawl_test
    )

    parser.start()
