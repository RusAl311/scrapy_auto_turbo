import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
import cfscrape

from ..items import OldAutosItemLoader, OldAutoItem


# pages = int(input('How many pages do you want to scrape: '))



class OldAutoSpider(CrawlSpider):
    name = "old_autos"
    allowed_domains = ['turbo.az']
    start_urls = ['https://turbo.az/autos/%s' % page for page in range(3895724, 603621, -1)]

    # def start_requests(self):
    #     """
    #     :param self:
    #     """
    #     try:
    #         token = cfscrape.get_tokens(OldAutoSpider.start_urls[0])
    #         for url in OldAutoSpider.start_urls:
    #             yield scrapy.Request(
    #                 url=url,
    #                 cookies=token,
    #             )

    custom_settings = {
        'ITEM_PIPELINES': {
            'auto.pipelines.SaveOldAutosPipeline': 200,
            'auto.pipelines.OldAutoPipeline': 300,
        },
        'DOWNLOAD_DELAY': 2,
        'ROBOTSTXT_OBEY': True,
        'COOKIES_ENABLED': False,
        # 'ROTATING_PROXY_LIST': [
        #     'http://smzrwyhr-dest:rqbu6c1p620k@209.127.191.180:80',
        #     'http://smzrwyhr-dest:rqbu6c1p620k@193.8.56.119:80',
        #     'http://smzrwyhr-dest:rqbu6c1p620k@185.164.56.20:80',
        #     'http://smzrwyhr-dest:rqbu6c1p620k@45.130.255.243:80',
        #     'http://smzrwyhr-dest:rqbu6c1p620k@45.95.96.132:80',
        #     'http://smzrwyhr-dest:rqbu6c1p620k@45.95.96.237:80',
        # ],
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
