from auto import pipelines
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from auto.items import SalonsItemLoader, SalonItem
import datetime

# pages = int(input('How many pages do you want to scrape: '))


class AutoSalonSpider(CrawlSpider):
    name = "salon_autos"
    allowed_domains = ['turbo.az']
    start_urls = [
        'https://turbo.az/avtosalonlar',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'auto.pipelines.SaveSalonsPipeline': 200,
            'auto.pipelines.SalonPipeline': 300,
        }
    }
    # pipelines = set([
    #     'auto.pipelines.SaveSalonsPipeline',
    #     'auto.pipelines.SalonPipeline',
    # ])

    rules = (
        # Rule(
        #     LinkExtractor(
        #         restrict_xpaths=['//div[@class="pagination-container"]/nav[@class="pagination"]/span[@class="next"]/a']
        #     ), callback='parse_auto', follow=True
        # ),
        Rule(
            LinkExtractor(
                restrict_xpaths=['//a[@class="shops-i featured"]']
            ), callback='parse_dealer_auto', follow=True
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths=['//a[@class="products-i-link"]']
            ), callback='parse_dealer_auto', follow=False
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths=['//a[@class="shops-i"]']
            ), callback='parse_salon_auto', follow=True
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths=['//a[@class="products-i-link"]']
            ), callback='parse_salon_auto', follow=False
        ),

    )

    def parse_salon_auto(self, response):
        selector = Selector(response)
        s = SalonsItemLoader(SalonItem(), selector)
        exists = response.xpath('//div[@class="product-properties-container"]').extract_first()
        manat = response.xpath('//div[@class="product-price"]/span/text()').extract_first()

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
            s.add_xpath('order', '//div[@class="product-statistics"]/p[3]/text()')
            s.add_value('isdealer', 0)

            if (manat == "AZN"):
                s.add_xpath('pricem', '//div[@class="product-price"]/text()')
                s.add_value('priced', '1')
            else:
                s.add_xpath('priced', '//div[@class="product-price"]/text()')
                s.add_value('pricem', '1')
            
            s.add_xpath('new', '//ul[@class="product-properties"]/li[13]/div[@class="product-properties-value"]/text()')
            s.add_xpath('salonname', '//a[@class="shop-contact--shop-name"]/text()')
            s.add_value('adddate', datetime.datetime.now())


            return s.load_item()

    def parse_dealer_auto(self, response):
        selector = Selector(response)
        d = SalonsItemLoader(SalonItem(), selector)
        exists = response.xpath('//div[@class="product-properties-container"]').extract_first()
        manat = response.xpath('//div[@class="product-price"]/span/text()').extract_first()

        if exists:
            d.add_xpath('city', '//li[@class="product-properties-i"]/div[@class="product-properties-value"]/text()')
            d.add_xpath('brand', '//ul[@class="product-properties"]/li[2]/div[@class="product-properties-value"]/a/text()')
            d.add_xpath('model', '//ul[@class="product-properties"]/li[3]/div[@class="product-properties-value"]/a/text()')
            d.add_xpath('year', '//ul[@class="product-properties"]/li[4]/div[@class="product-properties-value"]/a/text()')
            d.add_xpath('bodytype', '//ul[@class="product-properties"]/li[5]/div[@class="product-properties-value"]/text()')
            d.add_xpath('color', '//ul[@class="product-properties"]/li[6]/div[@class="product-properties-value"]/text()')
            d.add_xpath('engine', '//ul[@class="product-properties"]/li[7]/div[@class="product-properties-value"]/text()')
            d.add_xpath('power', '//ul[@class="product-properties"]/li[8]/div[@class="product-properties-value"]/text()')
            d.add_xpath('fuel', '//ul[@class="product-properties"]/li[9]/div[@class="product-properties-value"]/text()')
            d.add_xpath('mileage', '//ul[@class="product-properties"]/li[10]/div[@class="product-properties-value"]/text()')
            d.add_xpath('transmission', '//ul[@class="product-properties"]/li[11]/div[@class="product-properties-value"]/text()')
            d.add_xpath('drivetype', '//ul[@class="product-properties"]/li[12]/div[@class="product-properties-value"]/text()')
            d.add_xpath('order', '//div[@class="product-statistics"]/p[3]/text()')
            d.add_value('isdealer', 1)

            if (manat == "AZN"):
                d.add_xpath('pricem', '//div[@class="product-price"]/text()')
                d.add_value('priced', '1')
            else:
                d.add_xpath('priced', '//div[@class="product-price"]/text()')
                d.add_value('pricem', '1')
            
            d.add_xpath('new', '//ul[@class="product-properties"]/li[13]/div[@class="product-properties-value"]/text()')
            d.add_xpath('salonname', '//a[@class="shop-contact--shop-name"]/text()')
            d.add_value('adddate', datetime.datetime.now())


            return d.load_item()