from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

def _crawl(result, spider):
    deferred = process.crawl(spider)
    deferred.addCallback(_crawl, spider)
    return deferred

# process.crawl("autos")
_crawl(None, "autos")
process.start()
