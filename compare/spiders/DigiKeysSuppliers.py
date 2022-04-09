import scrapy


class DigikeyssuppliersSpider(scrapy.Spider):
    name = 'DigiKeysSuppliers'
    allowed_domains = ['www.digikey.com']
    start_urls = ['https://www.digikey.com/en/supplier-centers']

   
    def parse(self, response):
        for link in response.xpath('//ul[@class="supplier-group-list"]/li[@class="supplier-list-item"]/a[@class="dk-link"]/@href'):
            relative_link=link.get()
            yield response.follow(relative_link, callback=self.parse_suppliers)
    
    def parse_suppliers(self, response):
        for suppliers in response.xpath('//div[@id="main-layout-content"]'):
            try:
                about = suppliers.xpath('.//div[@class="about-supplier-paragraphs"]/p/text()').getall()
                yield {
                    "Supplier": suppliers.xpath('.//h1[@class="smc-h1-supplier-name"]/text()').get().strip(),
                    "About": about[0]
                }
            except:
                yield {
                    "Manufacturer":suppliers.xpath('//h1[@class="smc-h1-supplier-name"]/text()').get().strip(),
                    "About":suppliers.xpath('//div[@class="about-supplier-paragraphs"]/text()')
                }