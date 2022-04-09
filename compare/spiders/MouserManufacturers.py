import scrapy


class MousermanufacturersSpider(scrapy.Spider):
    name = 'MouserManufacturers'
    allowed_domains = ['www.mouser.co.uk']
    start_urls = ['https://www.mouser.co.uk/manufacturer/']

    def parse(self, response):
        for link in response.xpath('//ul[@class="list-unstyled mfr-category-list-items"]/li/a/@href'):
            relative_url= link.get()
            yield response.follow(relative_url, callback=self.parse_manufacturers)
    
    def parse_manufacturers(self, response):
        for manufacturer in response.xpath('//main[@role="main"]'):
            try:
                yield {
                    "Manufacturer": manufacturer.xpath('.//h1[@class="h1_about"]/text()').get().strip(),
                    "About":manufacturer.xpath('.//div[@id="supplier_content"]/p/text()').get().replace(", ", "")
                }
            except:
                yield {
                    "Manufacturer": manufacturer.xpath('.//h1[@class="h1_about"]/text()').get().strip(),
                    "About":'null'
                }
        
