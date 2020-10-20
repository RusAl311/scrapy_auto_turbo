from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from auto.items import AutosItemLoader, AutoItem

# pages = int(input('How many pages do you want to scrape: '))


class AutoSpider(CrawlSpider):
    name = "autos"
    allowed_domains = ['turbo.az']
    start_urls = ['https://turbo.az/autos']
    # start_urls = ['https://turbo.az/']

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=['//a[@class="products-i-link"]']
            ), callback='parse_auto', follow=False
        ),
        # Rule(
        #     LinkExtractor(
        #         restrict_xpaths=['//nav[@class="pagination"]/span[@class="next"]/a']
        #     ), callback='parse_auto', follow=True
        # ),
    )

    def parse_auto(self, response):
        exists = response.xpath('//div[@class="product-properties-container"]').extract_first()
        salon = response.xpath('//div[@class="products-i vipped salon"]').extract_first()
        selector = Selector(response)
        l = AutosItemLoader(AutoItem(), selector)
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
                l.add_xpath('price', '//div[@class="product-price"]/text()')
                l.add_xpath('order', '//div[@class="product-statistics"]/p[3]/text()')
                l.add_xpath('name', '//div[@class="seller-name"]/p/text()')
                l.add_xpath('number', '//div[@class="seller-phone"]/a/text()')
            
            return l.load_item()
        # for a in response.xpath('div[@class="pagination-container"]/nav/span[@class="next"]/a'):
        #     yield response.follow(a, self.parse_auto)


    def parse_salon_auto(self, response):
        pass
