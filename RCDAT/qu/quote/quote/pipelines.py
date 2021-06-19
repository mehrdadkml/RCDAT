# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3

class QuotePipeline:
    def __init__(self):
        self.create_connection()
        self.create_teble()

    def create_connection(self):
        self.conn=sqlite3.connect("maycoins.db")
        self.curr=self.conn.cursor()

    def create_teble(self):
        self.curr.execute(""" DROP TABLE IF EXISTS coins_tb""" )
        self.curr.execute("""create table coins_tb(
                name text,
                volume text,
                marketcap text
        
                 )""" )


    def process_item(self, items, spider):
        self.store_db(items)
        print("pipeline:"+items["name"][0])
        return items

    def store_db(self,items):
        self.curr("""insert into coins_tb values (?,?,?) """,(
            items["name"][0],
            items["volume"][0],
            items["marketcap"][0]
        ))
        self.conn.commit()