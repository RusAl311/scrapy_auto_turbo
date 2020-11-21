from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from twisted.internet.task import deferLater

def sleep(self, *args, seconds):
    """Non blocking sleep callback"""
    return deferLater(reactor, seconds, lambda: None)

def crash(failure):
    print('oops, spider crashed')
    print(failure.getTraceback())

process = CrawlerProcess(get_project_settings())

def _crawl(result, spider):
    deferred = process.crawl(spider)
    deferred.addCallback(lambda results: print('waiting 100 seconds before restart...'))
    deferred.addErrback(crash)  # <-- add errback 
    deferred.addCallback(sleep, seconds=1000)
    deferred.addCallback(_crawl, spider)
    return deferred

# process.crawl("autos")
_crawl(None, "salon_autos")
process.start()
