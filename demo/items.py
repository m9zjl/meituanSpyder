# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import item, Field


class ShopInfos(scrapy.Item):
    # define the fields for your item here like:
    phone = scrapy.Field()
    cityId = scrapy.Field()
    location = scrapy.Field()
    addr = scrapy.Field()
    brandId = scrapy.Field()
    groupInfo = scrapy.Field()
    parkingInfo = scrapy.Field()
    isSnack = scrapy.Field()
    discount = scrapy.Field()
    avgPrice = scrapy.Field()
    floor = scrapy.Field()
    avgScore = scrapy.Field()
    poiid = scrapy.Field()
    dayRoomSpan = scrapy.Field()
    lowestPrice = scrapy.Field()
    introduction = scrapy.Field()
    isExclusive = scrapy.Field()
    payAbstracts = scrapy.Field()
    lng = scrapy.Field()
    markNumbers = scrapy.Field()
    lat = scrapy.Field()
    areaId = scrapy.Field()
    subwayStatioinId = scrapy.Field()
    name = scrapy.Field()
    referenctPrice = scrapy.Field()
    featureMenu = scrapy.Field()
    isWaimai = scrapy.Field()
    isHot = scrapy.Field()
    hasGroup = scrapy.Field()
    isImax = scrapy.Field()
    wifi = scrapy.Field()
    abstracts = scrapy.Field()
    allowRefund = scrapy.Field()
    openInfo = scrapy.Field()
    cateName = scrapy.Field()
