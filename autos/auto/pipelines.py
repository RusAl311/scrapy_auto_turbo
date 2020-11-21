# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from auto.models import Auto, SalonAuto, OldAuto, db_connect, create_table


class AutoPipeline(object):
    def process_item(self, item, spider):
        return item

class SaveAutosPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        auto = Auto()
        auto.city = item["city"]
        auto.brand = item["brand"]
        auto.model = item["model"]
        auto.year = item["year"]
        auto.bodytype = item["bodytype"]
        auto.color = item["color"]
        auto.engine = item["engine"]
        auto.power = item["power"]
        auto.fuel = item["fuel"]
        auto.mileage = item["mileage"]
        auto.transmission = item["transmission"]
        auto.drivetype = item["drivetype"]
        auto.new = item["new"]
        auto.pricem = item["pricem"]
        auto.priced = item["priced"]
        auto.order = item["order"]
        auto.name = item["name"]
        auto.number = item["number"]
        auto.adddate = item["adddate"]

        order_exist = session.query(Auto).filter_by(order = auto.order).first()
        if  order_exist is not None: # the current order exists
            if order_exist.priced == 1:
                order_exist.priced = order_exist.pricem / 1.7

            if order_exist.pricem == 1:
                order_exist.pricem = 1.7 * order_exist.priced

            if auto.priced == order_exist.priced:
                order_exist.order = None
            else:
                 auto.priced = order_exist.priced
                 auto.order = order_exist.order

            if auto.pricem == order_exist.pricem:
                order_exist.order = None
            else:
                auto.pricem == order_exist.pricem
                auto.order = order_exist.order
            print('Exist', auto.order)
        else:
            auto.order = item["order"]
            print(auto.order)

        if auto.pricem == 1:
            auto.pricem = 1.7 * auto.priced

        if auto.priced == 1:
            auto.priced = auto.pricem / 1.7


        try:
            session.add(auto)
            session.commit()
        
        except:
            session.rollback()
            raise
        
        finally:
            session.close()
        
        return item


class SalonPipeline(object):
    def process_item(self, item, spider):
        return item

class SaveSalonsPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        salon = SalonAuto()
        salon.city = item["city"]
        salon.brand = item["brand"]
        salon.model = item["model"]
        salon.year = item["year"]
        salon.bodytype = item["bodytype"]
        salon.color = item["color"]
        salon.engine = item["engine"]
        salon.power = item["power"]
        salon.fuel = item["fuel"]
        salon.mileage = item["mileage"]
        salon.transmission = item["transmission"]
        salon.drivetype = item["drivetype"]
        salon.new = item["new"]
        salon.pricem = item["pricem"]
        salon.priced = item["priced"]
        salon.order = item["order"]
        salon.isdealer = item["isdealer"]
        salon.adddate = item["adddate"]
        salon.salonname = item["salonname"]

        order_exist = session.query(SalonAuto).filter_by(order = salon.order).first()
        if  order_exist is not None: # the current order exists
            if order_exist.priced == 1:
                order_exist.priced = order_exist.pricem / 1.7

            if order_exist.pricem == 1:
                order_exist.pricem = 1.7 * order_exist.priced

            if salon.priced == order_exist.priced:
                order_exist.order = None
            else:
                 salon.priced = order_exist.priced
                 salon.order = order_exist.order

            if salon.pricem == order_exist.pricem:
                order_exist.order = None
            else:
                salon.pricem == order_exist.pricem
                salon.order = order_exist.order
            print('Exist', salon.order)
        else:
            salon.order = item["order"]
            print(salon.order)

        if salon.pricem == 1:
            salon.pricem = 1.7 * salon.priced

        if salon.priced == 1:
            salon.priced = salon.pricem / 1.7


        try:
            session.add(salon)
            session.commit()
        
        except:
            session.rollback()
            raise
        
        finally:
            session.close()
        
        return item

class OldAutoPipeline(object):
    def process_item(self, item, spider):
        return item

class SaveOldAutosPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        oldauto = OldAuto()
        oldauto.city = item["city"]
        oldauto.brand = item["brand"]
        oldauto.model = item["model"]
        oldauto.year = item["year"]
        oldauto.bodytype = item["bodytype"]
        oldauto.color = item["color"]
        oldauto.engine = item["engine"]
        oldauto.power = item["power"]
        oldauto.fuel = item["fuel"]
        oldauto.mileage = item["mileage"]
        oldauto.transmission = item["transmission"]
        oldauto.drivetype = item["drivetype"]
        oldauto.new = item["new"]
        oldauto.pricem = item["pricem"]
        oldauto.priced = item["priced"]
        oldauto.order = item["order"]
        oldauto.adddate = item["adddate"]

        order_exist = session.query(OldAuto).filter_by(order = oldauto.order).first()
        if  order_exist is not None: # the current order exists
            if order_exist.priced == 1:
                order_exist.priced = order_exist.pricem / 1.7

            if order_exist.pricem == 1:
                order_exist.pricem = 1.7 * order_exist.priced

            if oldauto.priced == order_exist.priced:
                order_exist.order = None
            else:
                 oldauto.priced = order_exist.priced
                 oldauto.order = order_exist.order

            if oldauto.pricem == order_exist.pricem:
                order_exist.order = None
            else:
                oldauto.pricem == order_exist.pricem
                oldauto.order = order_exist.order
            print('Exist', oldauto.order)
        else:
            oldauto.order = item["order"]
            print(oldauto.order)

        if oldauto.pricem == 1:
            oldauto.pricem = 1.7 * oldauto.priced

        if oldauto.priced == 1:
            oldauto.priced = oldauto.pricem / 1.7


        try:
            session.add(oldauto)
            session.commit()
        
        except:
            session.rollback()
            raise
        
        finally:
            session.close()
        
        return item

