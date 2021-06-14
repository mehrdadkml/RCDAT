FROM python:3.8-alpine

COPY . /app

WORKDIR /app

RUN pip install scrapy

RUN pip install scrapyrt

RUN scrapy crawl coin -o coin.json

RUN scrapyrt -p 3000

# enter in url http://localhost:3000/crawl.json?start_requests=true&spider_name=coin

CMD ["python" ]