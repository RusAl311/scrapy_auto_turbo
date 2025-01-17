# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
# from scrapy.loader.processors import TakeFirst, MapCompose
from itemloaders.processors import TakeFirst, MapCompose
from datetime import datetime


def proceed_date(text):
    if (text is not None):
        text = text.strip(': ')
        text = text.replace('Yanvar', '01')
        text = text.replace('Fevral', '02')
        text = text.replace('Mart', '03')
        text = text.replace('Aprel', '04')
        text = text.replace('May', '05')
        text = text.replace('İyun', '06')
        text = text.replace('İyul', '07')
        text = text.replace('Avqust', '08')
        text = text.replace('Sentyabr', '09')
        text = text.replace('Oktyabr', '10')
        text = text.replace('Noyabr', '11')
        text = text.replace('Dekabr', '12')

        text = text.replace(' ', '/')
        text = datetime.strptime(text, '%d/%m/%Y').date()
        return text

def proceed_usd(text):
    if (text is not None):
        text = text.strip().replace(' ', '')
        text = int(text)
        return text

def proceed_manat(text):
    if (text is not None):    
        text = text.strip().replace(' ', '')
        text = int(text)
        return text

def remove_engine(text):
    text = text.strip(' L')
    text = float(text)
    return text

def remove_power(text):
    text = text.strip(' a.g.')
    text = int(text)
    return text

def remove_mileage(text):
    text = text.strip(' km').replace(' ', '')
    text = int(text)
    return text

def remove_order(text):
    text = text.strip(': ')
    text = int(text)
    return text

def remove_price(text):
    text = text.strip().replace(' ', '')
    text = int(text)
    return text

def normalize_new(text):
    if (text == 'Xeyr'):
        text = text.replace('Xeyr', '0')
        text = int(text)
        return text
    else:
        text = text.replace('Bəli', '1')
        text = int(text)
        return text


class AutoItem(scrapy.Item):
    city = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    bodytype = scrapy.Field()
    color = scrapy.Field()
    engine = scrapy.Field()
    power = scrapy.Field()
    fuel = scrapy.Field()
    mileage = scrapy.Field()
    transmission = scrapy.Field()
    drivetype = scrapy.Field()
    new = scrapy.Field()
    pricem = scrapy.Field()
    priced = scrapy.Field()
    order = scrapy.Field()
    salon = scrapy.Field()
    name = scrapy.Field()
    number = scrapy.Field()
    adddate = scrapy.Field()


class AutosItemLoader(ItemLoader):
    city_out = TakeFirst()
    brand_out = TakeFirst()
    model_out = TakeFirst()
    year_out = TakeFirst()
    bodytype_out = TakeFirst()
    color_out = TakeFirst()
    engine_in = MapCompose(remove_engine)
    engine_out = TakeFirst()
    power_in = MapCompose(remove_power)
    power_out = TakeFirst()
    fuel_out = TakeFirst()
    mileage_in = MapCompose(remove_mileage)
    mileage_out = TakeFirst()
    transmission_out = TakeFirst()
    drivetype_out = TakeFirst()
    new_in = MapCompose(normalize_new)
    new_out = TakeFirst()
    pricem_in = MapCompose(proceed_manat)
    pricem_out = TakeFirst()
    priced_in = MapCompose(proceed_usd)
    priced_out = TakeFirst()
    order_in = MapCompose(remove_order)
    order_out = TakeFirst()
    salon_out = TakeFirst()
    name_out = TakeFirst()
    number_out = TakeFirst() 
    adddate_out = TakeFirst()

class SalonItem(scrapy.Item):
    city = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    bodytype = scrapy.Field()
    color = scrapy.Field()
    engine = scrapy.Field()
    power = scrapy.Field()
    fuel = scrapy.Field()
    mileage = scrapy.Field()
    transmission = scrapy.Field()
    drivetype = scrapy.Field()
    new = scrapy.Field()
    pricem = scrapy.Field()
    priced = scrapy.Field()
    order = scrapy.Field()
    isdealer = scrapy.Field()
    salonname = scrapy.Field()
    adddate = scrapy.Field()

class SalonsItemLoader(ItemLoader):
    city_out = TakeFirst()
    brand_out = TakeFirst()
    model_out = TakeFirst()
    year_out = TakeFirst()
    bodytype_out = TakeFirst()
    color_out = TakeFirst()
    engine_in = MapCompose(remove_engine)
    engine_out = TakeFirst()
    power_in = MapCompose(remove_power)
    power_out = TakeFirst()
    fuel_out = TakeFirst()
    mileage_in = MapCompose(remove_mileage)
    mileage_out = TakeFirst()
    transmission_out = TakeFirst()
    drivetype_out = TakeFirst()
    new_in = MapCompose(normalize_new)
    new_out = TakeFirst()
    pricem_in = MapCompose(proceed_manat)
    pricem_out = TakeFirst()
    priced_in = MapCompose(proceed_usd)
    priced_out = TakeFirst()
    order_in = MapCompose(remove_order)
    order_out = TakeFirst()
    isdealer_out = TakeFirst()
    salonname_out = TakeFirst()
    adddate_out = TakeFirst()

class OldAutoItem(scrapy.Item):
    city = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    bodytype = scrapy.Field()
    color = scrapy.Field()
    engine = scrapy.Field()
    power = scrapy.Field()
    fuel = scrapy.Field()
    mileage = scrapy.Field()
    transmission = scrapy.Field()
    drivetype = scrapy.Field()
    new = scrapy.Field()
    pricem = scrapy.Field()
    priced = scrapy.Field()
    order = scrapy.Field()
    adddate = scrapy.Field()


class OldAutosItemLoader(ItemLoader):
    city_out = TakeFirst()
    brand_out = TakeFirst()
    model_out = TakeFirst()
    year_out = TakeFirst()
    bodytype_out = TakeFirst()
    color_out = TakeFirst()
    engine_in = MapCompose(remove_engine)
    engine_out = TakeFirst()
    power_in = MapCompose(remove_power)
    power_out = TakeFirst()
    fuel_out = TakeFirst()
    mileage_in = MapCompose(remove_mileage)
    mileage_out = TakeFirst()
    transmission_out = TakeFirst()
    drivetype_out = TakeFirst()
    new_in = MapCompose(normalize_new)
    new_out = TakeFirst()
    pricem_in = MapCompose(proceed_manat)
    pricem_out = TakeFirst()
    priced_in = MapCompose(proceed_usd)
    priced_out = TakeFirst()
    order_in = MapCompose(remove_order)
    order_out = TakeFirst()
    adddate_in = MapCompose(proceed_date)
    adddate_out = TakeFirst()