from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from auto.items import AutosItemLoader, AutoItem, SalonsItemLoader, SalonItem
import datetime

# pages = int(input('How many pages do you want to scrape: '))


class AutoSpider(CrawlSpider):
    name = "salon_autos"
    allowed_domains = ['turbo.az']
    start_urls = [
        'https://turbo.az/avtosalonlar',
    ]

    rules = (
        # Rule(
        #     LinkExtractor(
        #         restrict_xpaths=['//div[@class="pagination-container"]/nav[@class="pagination"]/span[@class="next"]/a']
        #     ), callback='parse_auto', follow=True
        # ),
        Rule(
            LinkExtractor(
                restrict_xpaths=['//a[@class="products-i-link"]']
            ), callback='parse_auto', follow=False
        ),
    )

    def parse_auto(self, response):
        exists = response.xpath('//div[@class="product-properties-container"]').extract_first()
        salon = response.xpath('//div[@class="products-i vipped salon"]').extract()
        manat = response.xpath('//div[@class="product-price"]/span/text()').extract_first()
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
                if (manat == "AZN"):
                    l.add_xpath('pricem', '//div[@class="product-price"]/text()')
                    l.add_value('priced', '1')
                else:
                    l.add_xpath('priced', '//div[@class="product-price"]/text()')
                    l.add_value('pricem', '1')
                l.add_xpath('order', '//div[@class="product-statistics"]/p[3]/text()')
                l.add_xpath('name', '//div[@class="seller-name"]/p/text()')
                l.add_xpath('number', '//div[@class="seller-phone"]/a/text()')
                l.add_value('adddate', datetime.datetime.now())
                
            
            return l.load_item()
        


    def parse_salon_auto(self, response):
        selector = Selector(response)
        s = SalonsItemLoader(SalonItem(), selector)
        exists = response.xpath('//div[@class="product-properties-container"]').extract_first()
        if exists:
            s.add_xpath('city', '//li[@class="product-properties-i"]/div[@class="product-properties-value"]/text()')
            s.add_xpath('brand', '//ul[@class="product-properties"]/li[2]/div[@class="product-properties-value"]/a/text()')
            s.add_xpath('model', '//ul[@class="product-properties"]/li[3]/div[@class="product-properties-value"]/a/text()')
            s.add_xpath('year', '//ul[@class="product-properties"]/li[4]/div[@class="product-properties-value"]/a/text()')
            s.add_xpath('bodytype', '//ul[@class="product-properties"]/li[5]/div[@class="product-properties-value"]/text()')
            s.add_xpath('color', '//ul[@class="product-properties"]/li[6]/div[@class="product-properties-value"]/text()')
            s.add_xpath('engine', '//ul[@class="product-properties"]/li[7]/div[@class="product-properties-value"]/text()')
            s.add_xpath('power', '//ul[@class="product-properties"]/li[8]/div[@class="product-properties-value"]/text()')
            s.add_xpath('fuel', '//ul[@class="product-properties"]/li[9]/div[@class="product-properties-value"]/text()')
            s.add_xpath('mileage', '//ul[@class="product-properties"]/li[10]/div[@class="product-properties-value"]/text()')
            s.add_xpath('transmission', '//ul[@class="product-properties"]/li[11]/div[@class="product-properties-value"]/text()')
            s.add_xpath('drivetype', '//ul[@class="product-properties"]/li[12]/div[@class="product-properties-value"]/text()')

            return s.load_item()


