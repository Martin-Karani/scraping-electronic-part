import scrapy


class SourceerbdistributorsSpider(scrapy.Spider):
    name = 'SourceerbDistributors'
    allowed_domains = ['sourceesb.com']
    start_urls = [
    'https://sourceesb.com/distributors/0-9~1',
    'https://sourceesb.com/distributors/A~1',
    'https://sourceesb.com/distributors/B~1',
    'https://sourceesb.com/distributors/C~1',
    'https://sourceesb.com/distributors/D~1',
    'https://sourceesb.com/distributors/E~1',
    'https://sourceesb.com/distributors/F~1',
    'https://sourceesb.com/distributors/G~1',
    'https://sourceesb.com/distributors/H~1',
    'https://sourceesb.com/distributors/I~1',
    'https://sourceesb.com/distributors/J~1',
    'https://sourceesb.com/distributors/K~1',
    'https://sourceesb.com/distributors/L~1',
    'https://sourceesb.com/distributors/M~1',
    'https://sourceesb.com/distributors/N~1',
    'https://sourceesb.com/distributors/O~1',
    'https://sourceesb.com/distributors/P~1',
    'https://sourceesb.com/distributors/Q~1',
    'https://sourceesb.com/distributors/R~1',
    'https://sourceesb.com/distributors/S~1',
    'https://sourceesb.com/distributors/T~1',
    'https://sourceesb.com/distributors/U~1',
    'https://sourceesb.com/distributors/V~1',
    'https://sourceesb.com/distributors/W~1',
    'https://sourceesb.com/distributors/X~1',
    'https://sourceesb.com/distributors/Y~1',
    'https://sourceesb.com/distributors/Z~1',
    ]

    def parse(self, response):
        for link in  response.xpath('//ul[@class="listing"]/li/a/@href'):
            relative_url= link.get()
            yield response.follow(relative_url, callback=self.parse_distributors)
        
        next_page_url = response.xpath('//div[@class="listing__pager"]/ul/li[@class="next"]/a/@href');

        if next_page_url is not None:
             yield scrapy.Request(response.urljoin(next_page_url),callback=self.parse)

    def parse_distributors(self, response):
        for distributor in response.xpath('//div[@class="company-info"]'):
            try:
                yield {
                    "Manufacturer": distributor.xpath('.//div[@class="company-info__title"]/h1/text()').get(),
                    "About":distributor.xpath('.//div[@class="company-info__text"]/p[@class="company-info__description"]/text()').get()
                }
            except:
                yield {
                    "Manufacturer": distributor.xpath('.//div[@class="company-info__title"]/h1/text()').get(),
                    "About":'null'
                }
        
