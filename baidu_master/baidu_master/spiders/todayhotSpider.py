#from scrapy_redis.spiders import RedisSpider
import scrapy
from baidu_master.utils.insertRedis import inserintota


class todayhotSpider(scrapy.Spider):
    name = "todayhotSpider"
    #allowed_domains = ["top.baidu.com"]
    start_urls = ["http://top.baidu.com/buzz?b=341&c=513&fr=topcategory_c513"]
    redis_key = "todayhotInfoSpider:start_urls"

    def parse(self, response):
        hot_list = response.xpath("//a[@class='list-title']/attribute::href").extract()
        for i in hot_list:
            inserintota("todayhotInfoSpider:start_urls", i)
            # inserintota(redis_key, i)
            print ('[success] the detail link ' + i + ' is insert into the redis queue')