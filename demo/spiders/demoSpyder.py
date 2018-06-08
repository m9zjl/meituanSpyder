# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from ..items import ShopInfos

class meituanSpyder(scrapy.Spider):
    name = "demo"
    index = 0
    epoch = 25
    city_id = 55
    total_count = 0;
    url = 'http://api.meituan.com/group/v4/deal/select/city/{0}/cate/1?sort=solds&hasGroup=true&mpt_cate1=1&offset={1}&limit={2}'
    def start_requests(self):
        # url = '﻿http://api.meituan.com/group/v4/deal/select/city/94/cate/1?sort=solds&hasGroup=true&mpt_cate1=1&offset={0}&limit={1}'
        # for i in range(10):
        url = self.url.format(self.city_id, self.index*self.epoch, self.epoch)
        yield Request(url)

    def parse(self, response):
        info_json = json.loads(response.text)
        response_length = len(info_json['data'])
        self.total_count = self.total_count + response_length
        print("返回商家列表%d,总得到商家列表%d" % (response_length, self.total_count))
        # response lenth zero means all visited
        if response_length == 0:
            print('城市%d遍历完毕'%(self.city_id))
            return
        # deal with response if response lenth is not 0
        items = []
        for item in info_json['data']:
            item = item['poi']
            shopeinfo = ShopInfos()
            shopeinfo['phone'] = item['phone']
            shopeinfo['cityId'] = item['cityId']
            shopeinfo['location'] = item['location']
            shopeinfo['addr'] = item['addr']
            shopeinfo['brandId'] = item['brandId']
            shopeinfo['groupInfo'] = item['groupInfo']
            shopeinfo['parkingInfo'] = item['parkingInfo']
            shopeinfo['isSnack'] = item['isSnack']
            shopeinfo['discount'] = item['discount']
            shopeinfo['avgPrice'] = item['avgPrice']
            shopeinfo['floor'] = item['floor']
            shopeinfo['avgScore'] = item['avgScore']
            shopeinfo['dayRoomSpan'] = item['dayRoomSpan']
            shopeinfo['lowestPrice'] = item['lowestPrice']
            shopeinfo['introduction'] = item['introduction']
            shopeinfo['isExclusive'] = item['isExclusive']
            shopeinfo['payAbstracts'] = item['payAbstracts']
            shopeinfo['lng'] = item['lng']
            shopeinfo['markNumbers'] = item['markNumbers']
            shopeinfo['lat'] = item['lat']
            shopeinfo['areaId'] = item['areaId']
            shopeinfo['poiid'] = item['poiid']
            shopeinfo['subwayStatioinId'] = item['subwayStationId']
            shopeinfo['name'] = item['name']
            shopeinfo['referenctPrice'] = item['referencePrice']
            shopeinfo['featureMenu'] = item['featureMenus']
            shopeinfo['isWaimai'] = item['isWaimai']
            shopeinfo['isHot'] = item['isHot']
            shopeinfo['hasGroup'] = item['hasGroup']
            shopeinfo['isImax'] = item['isImax']
            shopeinfo['wifi'] = item['wifi']
            shopeinfo['abstracts'] = item['abstracts']
            shopeinfo['allowRefund'] = item['allowRefund']
            shopeinfo['openInfo'] = item['openInfo']
            shopeinfo['cateName'] = item['cateName']
            yield shopeinfo
        self.index = self.index + 1
        # response resolved, jump to the next url
        url = self.url.format(self.city_id,self.index*self.epoch, self.epoch)
        yield Request(url)


