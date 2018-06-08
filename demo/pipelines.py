# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import codecs
import sys
import json


class DemoPipeline(object):

    def process_item(self, item, spider):
        # 获取当前工作目录
        base_dir = os.getcwd()
        fiename = base_dir + '/items.txt'
        # 从内存以追加的方式打开文件，并写入对应的数据
        with codecs.open(fiename, 'a', 'utf-8') as f:
            for var in item:
                f.write(var + '\t')
            f.write('\n')
        return item


class JsonPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/items.json'
        # 打开json文件，向里面以dumps的方式吸入数据
        # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如
        with codecs.open(filename, 'a', 'utf-8') as f:
            json.dump(dict(item),f)
        return item
