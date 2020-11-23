from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

from ..items import OldAutosItemLoader, OldAutoItem


# pages = int(input('How many pages do you want to scrape: '))



class OldAutoSpider(CrawlSpider):
    name = "old_autos"
    allowed_domains = ['turbo.az']
    start_urls = ['https://turbo.az/autos/%s' % page for page in range(4059609, 603621, -1)]
    custom_settings = {
        'ITEM_PIPELINES': {
            'auto.pipelines.SaveOldAutosPipeline': 200,
            'auto.pipelines.OldAutoPipeline': 300,
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
        },
        'DOWNLOAD_DELAY': 1.5,
        'ROBOTSTXT_OBEY': True,
        'COOKIES_ENABLED': False,
        'ROTATING_PROXY_LIST': [
            '178.128.50.52:3128',
            '182.160.119.155:8080',
            '198.58.11.39:8080',
            '178.115.253.35:8080'
        ],
    }
    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//div[@class="product-body"]']
            ), callback='parse_auto', follow=False
        ),
    )

    def parse_auto(self, response):
        exists = response.xpath('//div[@class="product-properties-container"]').extract_first()
        salon = response.xpath('//div[@class="products-i vipped salon"]').extract()
        manat = response.xpath('//div[@class="product-price"]/span/text()').extract_first()
        selector = Selector(response)
        l = OldAutosItemLoader(OldAutoItem(), selector)
        if exists:
            if salon:
                pass
            else:
                l.add_xpath('city', '//li[@class="product-properties-i"]/div[@class="product-properties-value"]/text()')
                l.add_xpath('brand', '//ul[@class="product-properties"]/li[2]/div[@class="product-properties-value"]/a/text()')
                l.add_xpath('model', '//ul[@class="product-properties"]/li[3]/div[@class="product-properties-value"]/a/text()')
                l.add_xpath('year', '//ul[@class="product-properties"]/li[4]/div[@class="product-properties-value"]/a/text()')
                l.add_xpath('bodytype', '//ul[@class="product-properties"]/li[5]/div[@class="product-properties-value"]/text()')
                l.add_xpath('color', '//ul[@class="product-properties"]/li[6]/div[@class="product-properties-value"]/text()')
                l.add_xpath('engine', '//ul[@class="product-properties"]/li[7]/div[@class="product-properties-value"]/text()')
                l.add_xpath('power', '//ul[@class="product-properties"]/li[8]/div[@class="product-properties-value"]/text()')
                l.add_xpath('fuel', '//ul[@class="product-properties"]/li[9]/div[@class="product-properties-value"]/text()')
                l.add_xpath('mileage', '//ul[@class="product-properties"]/li[10]/div[@class="product-properties-value"]/text()')
                l.add_xpath('transmission', '//ul[@class="product-properties"]/li[11]/div[@class="product-properties-value"]/text()')
                l.add_xpath('drivetype', '//ul[@class="product-properties"]/li[12]/div[@class="product-properties-value"]/text()')
                l.add_xpath('new', '//ul[@class="product-properties"]/li[13]/div[@class="product-properties-value"]/text()')
                if (manat == "AZN"):
                    l.add_xpath('pricem', '//div[@class="product-price"]/text()')
                    l.add_value('priced', '1')
                else:
                    l.add_xpath('priced', '//div[@class="product-price"]/text()')
                    l.add_value('pricem', '1')
                l.add_xpath('order', '//div[@class="product-statistics"]/p[3]/text()')
                # l.add_value('adddate', datetime.datetime.now())
                l.add_xpath('adddate', '//div[@class="product-statistics"]/p[2]/text()')
                
            
            return l.load_item()
