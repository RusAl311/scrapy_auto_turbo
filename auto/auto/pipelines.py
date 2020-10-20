# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


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
        auto.price = item["price"]
        auto.order = item["order"]
        auto.name = item["name"]
        auto.number = item["number"]

        try:
            session.add(auto)
            session.commit()
        
        except:
            session.rollback()
            raise
        
        finally:
            session.close()
        
        return item