# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class OpenuserjsPipeline(object):



    def process_item(self, item, spider):
        db = pymysql.connect("localhost", "root", "root", "test")
        cursor = db.cursor()
        sql = "insert into userjs(name,version,author,ddesc,installs,rating,updated) values(%s,%s,%s,%s,%s,%s,%s)"
        lis=(item["name"],item["version"],item["author"],item["desc"],item["installs"],item["rating"],item["updated"])
        # try:
        cursor.execute(sql,lis)
        db.commit()
        # except:
        #     print(1)
        #     db.rollback()
        return item






