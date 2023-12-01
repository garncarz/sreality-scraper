import itertools

import scrapy

from . import models, settings


class AdSpider(scrapy.Spider):
    name = 'ad_spider'

    def start_requests(self):
        for page in itertools.count():
            yield scrapy.Request(
                'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1'
                f'&per_page=20&page={page}'
            )

    def parse(self, response):
        if models.Ad.query.count() > settings.MAX_ITEMS:
            raise scrapy.exceptions.CloseSpider('Enough items in DB')

        data = response.json()
        for estate in data['_embedded']['estates']:
            yield dict(
                hash_id=str(estate['hash_id']),
                title=estate['name'],
                image=estate['_links']['images'][0]['href'],
            )
