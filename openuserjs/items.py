# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class UserJsItem(scrapy.Item):
    name=scrapy.Field();
    version=scrapy.Field();
    author=scrapy.Field();
    desc=scrapy.Field();
    installs=scrapy.Field();
    rating=scrapy.Field();
    updated=scrapy.Field();

class OpenuserjsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
