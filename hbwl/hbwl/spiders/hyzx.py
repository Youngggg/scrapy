# -*- coding: utf-8 -*-

import scrapy
from hbwl.items import HbwlItem
from hbwl.util.Md5 import Md5
import re

# 行业资讯
class hyzx(scrapy.Spider):
    name = "hyzx"
    allowed_domains = ["hebwl.cn"]
    start_urls = ["http://www.hebwl.cn/a/xwzx/hyzx/index.html"]

    def parse(self, response):
        hyzx_list = response.xpath("//div[@class='al_wi center zy_dt']/div[@class='zy_ri']/ul[@class='zl_xw']/li").extract()

        for i in range(1, len(hyzx_list)+1):

            item = HbwlItem()
            item["url"] = response.xpath("//div[@class='zy_ri']/ul[@class='zl_xw']/li["+str(i)+"]/div[@class='xw_pr']/h1/a/attribute::href").extract()[0]
            item["title"] = response.xpath("//div[@class='zy_ri']/ul[@class='zl_xw']/li["+str(i)+"]/div[@class='xw_pr']/h1/a/text()").extract()[0]
            item["id"] = i

            yield scrapy.Request(
                url=item["url"],
                callback=self.parse_content,
                meta={'item': item}
            )


    def parse_content(self, response):
        item = response.meta['item']
        contents = response.xpath("//div[@class='zy_nj']/div//text()").extract()
        content = []
        for c in contents:
            c = re.sub(r'\s', '', c)
            if c:
                content.append(c)

        contents = '\n'.join(content)
        item["content"] = contents

        yield item




