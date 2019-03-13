from scrapy_redis.spiders import RedisSpider


class todayhotInfoSpider(RedisSpider):
    name = "todayhotInfoSpider"

    def parse(self, response):
        pass