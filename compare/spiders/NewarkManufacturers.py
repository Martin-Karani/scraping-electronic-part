
import scrapy


class NewarkmanufacturersSpider(scrapy.Spider):
    name = 'NewarkManufacturers'
    allowed_domains = ['www.newark.com']
    start_urls = ['https://www.newark.com/manufacturers']
    print('hello world')

    def parse(self, response):
        for link in response.css('div.manuSection li a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_manufacturers)
    
    def parse_manufacturers(self, response):
        for manufacturer in response.xpath('//main'):
            try:
                about = manufacturer.xpath('(.//section[@class="threeQuarter"]/div)[2]')
                yield {
                    "Manufacturer": manufacturer.xpath('.//nav[@id="breadcrumb"]/ul/li[@class="breadcrumb_current"]/text()').get().strip(),
                    "About":about.xpath('.//p/text()').get()
                }
            except:
                yield {
                    "Manufacturer":manufacturer.xpath('.//nav[@id="breadcrumb"]/ul/li[@class="breadcrumb_current"]/text()').get().strip(),
                    "About":'null'
                }
        
