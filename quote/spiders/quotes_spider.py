import scrapy
from ..items    import QuoteItem
import pandas
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
class QuoteSpider(scrapy.Spider):
    name="coin"
    start_urls=[
        "https://coinmarketcap.com/"
    ]
    @newrelic.agent.background_task()
    def parse(self, response):
        all_tr_coins=response.css('tbody')

        items=QuoteItem()

        for coin in all_tr_coins:

            name=coin.css(".iJjGCS::text").extract()
            volume=coin.css(".font_weight_500___2Lmmi::text").extract()
            marketcap=coin.css(".ieFnWP::text").extract()

            items["name"]=name
            items["volume"]=volume
            items["marketcap"]=marketcap


            yield items
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)