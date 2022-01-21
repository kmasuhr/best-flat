import requests as requests
import scrapy
from scrapy.http import HtmlResponse


class ParserUtil:
    @classmethod
    def parse_float(cls, data):
        if data is None:
            return data

        if isinstance(data, str):
            return float(data.replace(' ', '').replace(',', '.'))

        return float(data)

    @classmethod
    def parse_int(cls, data):
        if data is None:
            return data

        if isinstance(data, str):
            return int(data.replace(' ', ''))

        return int(data)

    @classmethod
    def number_of_rooms(cls, data):
        if data is None:
            return data

        try:
            return int(data.strip())
        except:
            return 0

    @classmethod
    def floor(cls, data):
        if data is None:
            return data

        if data == 'Parter' or data == 'parter':
            return 0

        try:
            return int(data.strip())
        except:
            return 0


def get_total_pages(base_url):
    try:
        url = f'{base_url}?strona=999'
        r = requests.get(url)

        response = HtmlResponse(url=url, body=r.content, encoding='utf-8').css('li.page-off')
        total_pages = int(response[-1].css('a::attr(data-page-number)').get())
    except:
        total_pages = 0

    return total_pages


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        base_urls = [
            'https://ogloszenia.trojmiasto.pl/nieruchomosci/e1i,32_1_87_2_7_31,has_hv,1,ikl,101_106,ri,3_,xi,2010_.html',
        ]

        for base_url in base_urls:
            total_pagesss = get_total_pages(base_url)

            for i in range(total_pagesss + 1):
                url = f'{base_url}?strona={i}'

                r = requests.get(url)
                response = HtmlResponse(url=url, body=r.content, encoding='utf-8')

                for flat in response.css('div.list__item'):
                    yield scrapy.Request(url=flat.css('a.link::attr(href)').get(), callback=self.parse)

    def parse(self, response: HtmlResponse, **kwargs):
        flat_id = response.css('ul.oglStats').css('li').css('span::text').get().strip()

        price = response.css('span.oglDetailsMoney::text').get()
        price_per_meter = response.css('div.oglField--cena_za_m2').css('span.oglDetailsMoney::text').get()

        floor = response.css('div.oglField--pietro').css('span.oglField__value::text').get()
        floor_in_total = response.css('div.oglField--l_pieter').css('span.oglField__value::text').get()

        number_of_rooms = response.css('div.oglField--l_pokoi').css('span.oglField__value::text').get()
        year = response.css('div.oglField--rok_budowy').css('span.oglField__value::text').get()

        yield {
            'id': flat_id,

            'price': ParserUtil.parse_float(price),
            'price_per_meter': ParserUtil.parse_float(price_per_meter),

            'floor': ParserUtil.number_of_rooms(floor),
            'floor_in_total': ParserUtil.parse_int(floor_in_total),
            'last_floor': ParserUtil.number_of_rooms(floor) == ParserUtil.parse_int(floor_in_total),

            'number_of_rooms': ParserUtil.number_of_rooms(number_of_rooms),
            'year': ParserUtil.parse_int(year),
            'url': response.url,
        }
