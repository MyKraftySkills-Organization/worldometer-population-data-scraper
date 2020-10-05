# Worldometer Population Data Scraper

1. Installation guide

> pip install -r requirements.txt

2. To Crawl the spider (From the directory containing scrapy.cfg)

> scrapy crawl countries

3. To generate a dataset

> scrapy crawl countries -o file.csv
> scrapy crawl countries -o data.json