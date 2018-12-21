# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from hbwl.util.db import DB

class HbwlPipeline(object):


    def __init__(self, dbConn):
        self.__dbConn = dbConn

    @classmethod
    def from_settings(cls, settings):
        dbConn = DB(settings['MYSQL_HOST'], settings['MYSQL_PORT'], settings['MYSQL_USER'], settings['MYSQL_PASSWD'],
                    settings['MYSQL_DBNAME'])
        return cls(dbConn)

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


    def process_item(self, item, spider):
        item_dict = dict(item)

        if "content" not in item_dict:
            item['content'] = ''

        sql = (''' INSERT INTO `hyzx` (`id`, `title`, `content`, `url`) '''
               ''' VALUES ("%s", "%s","%s", "%s")'''
               % (item['id'], item['title'], item['content'], item['url']) )

        return self.__dbConn.insert(sql)