# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from quote.settings import MONGO_DB, MONGO_URI
from sqlite3.dbapi2 import PARSE_COLNAMES
from typing import Collection
from pymongo import MongoClient


class MongoDbPipeline:
    Collection="coin"
    def __init__(self,mongo_uri,mongo_db):
       self.mongo_uri=mongo_uri
       self.mongo_db=mongo_db
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self,spider):
       self.client=MongoClient(self.mongo_uri)
       self.db=self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.Collection].insert_one(dict(item))
        return item
    # def store_db(self,items):
    #     self.curr("""insert into coins_tb values (?,?,?) """,(
    #         items["name"][0],
    #         items["volume"][0],
    #         items["marketcap"][0]
    #     ))
    #     self.conn.commit()