# -*- coding: utf-8 -*-
"""爬虫配置文件"""
import os


# MYSQL
MYSQL_IP = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "spider-demo"
MYSQL_USER_NAME = "spider"
MYSQL_USER_PASS = "test"

# REDIS
# IP:PORT 多个逗号分隔
REDISDB_IP_PORTS = "localhost:6379"
REDISDB_USER_PASS = ""
# 默认 0 到 15 共16个数据库
REDISDB_DB = 0