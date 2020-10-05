# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # Takes relative url
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

            # absolute_path = f"https://www.worldometers.info{link}"
            # absolute_path = response.urljoin(link)
            # Takes Absolute Url
            # yield scrapy.Reque st(url=absolute_path)

    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")

        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yearly_per_change = row.xpath(".//td[3]/text()").get()
            yearly_change = row.xpath(".//td[4]/text()").get()
            median_age = row.xpath(".//td[6]/text()").get()
            fertility_rate = row.xpath(".//td[7]/text()").get()
            country_share = row.xpath(".//td[11]/text()").get()
            world_population = row.xpath(".//td[12]/text()").get()
            global_rank = row.xpath(".//td[13]/text()").get()

            yield{
                'country_name': name,
                'year': year,
                'population': population,
                'yearly percent change': yearly_per_change,
                'yearly change': yearly_change,
                'median age': median_age,
                'fertility rate': fertility_rate,
                'country share of world population': country_share,
                'world population': world_population,
                'global rank': global_rank
            }
