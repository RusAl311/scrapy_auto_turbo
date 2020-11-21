from scrapy import settings
from scrapy import spiderloader
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

settings = get_project_settings()
spider_loader = spiderloader.SpiderLoader.from_settings(settings)
process = CrawlerProcess()

print('fdsfdfsfs', spider_loader.list())
for spider_name in spider_loader.list():
    print ("Running spider %s" % (spider_name))
    process.crawl(spider_name) 
process.start()


# from scrapy import spiderloader
# from twisted.internet.defer import inlineCallbacks
# from scrapy.crawler import CrawlerRunner
# from twisted.internet import reactor, defer
# from scrapy.utils.project import get_project_settings

# runner = CrawlerRunner()

# @defer.inlineCallbacks
# def crawl():
#     settings = get_project_settings()
#     spider_loader = spiderloader.SpiderLoader.from_settings(settings)
#     spiders = spider_loader.list()
#     classes = [spider_loader.load(name) for name in spiders]
#     for my_spider in classes:
#         print(my_spider)
#         yield runner.crawl(my_spider)
#     reactor.stop()

# crawl()
# reactor.run()