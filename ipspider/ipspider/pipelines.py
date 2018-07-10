# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

from ipspider.items import IpspiderItem


PROXY = [
    ]




class Ip_check_able(object):
    def __init__(self):
        connection = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db['Collection']

    def process_item(self, item, spider):
        if isinstance(item,IpspiderItem):
            data = {}
            for i in item.fields:
                data[i] = item[i]
            # self.collection.update({'host': data['host']}, {'$set': data}
            #                         , True)


            PROXY.append(data)
            print(PROXY)

        return item
