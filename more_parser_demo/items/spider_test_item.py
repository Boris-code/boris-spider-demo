# -*- coding: utf-8 -*-
'''
Created on 2020-07-13 13:04:43
---------
@summary:
---------
@author: liubo
'''

from spider import Item


class SpiderTestItem(Item):
    # __unique_key__ = ("title",)

    def __init__(self, *args, **kwargs):
        # self.id = None  # type : int(10) unsigned | allow_null : NO | key : PRI | default_value : None | extra : auto_increment | column_comment : 
        self.title = None  # type : varchar(255) | allow_null : YES | key :  | default_value : None | extra : | column_comment :
