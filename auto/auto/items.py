# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class AutoItem(scrapy.Item):
    url = scrapy.Field()
    city = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    body_type = scrapy.Field()
    color = scrapy.Field()
    engine = scrapy.Field()
    power = scrapy.Field()
    fuel = scrapy.Field()
    mileage = scrapy.Field()
    transmission = scrapy.Field()
    drive_type = scrapy.Field()
    new = scrapy.Field()
    price = scrapy.Field()
    order = scrapy.Field()
    salon = scrapy.Field()


class AutosItemLoader(ItemLoader):
    url_out = TakeFirst()
    city_out = TakeFirst()
    brand_out = TakeFirst()
    model_out = TakeFirst()
    year_out = TakeFirst()
    body_type_out = TakeFirst()
    color_out = TakeFirst()
    engine_out = TakeFirst()
    power_out = TakeFirst()
    fuel_out = TakeFirst()
    mileage_out = TakeFirst()
    transmission_out = TakeFirst()
    drive_type_out = TakeFirst()
    new_out = TakeFirst()
    price_out = TakeFirst()
    order_out = TakeFirst()
