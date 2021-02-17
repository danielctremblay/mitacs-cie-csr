import json
import scrapy
import logging

logger = logging.getLogger(__name__)

class SmmCaSpider(scrapy.Spider):
    name = 'smm_ca'
    allowed_domains = ['stockmarketmba.com']
    start_urls = ['https://stockmarketmba.com/canadiancompaniesthattradeonusexchanges.php/']

    def parse(self, response):

        # Parsing Canadian companies
        cies = response.xpath('//table[@id="ETFs"]/tbody/tr')

        cies_dict = {}

        for cie_tree in cies:
            fields = cie_tree.xpath('td')
            cie = {}
            cie['url'] =  fields[0].xpath('a/@href').extract_first()
            symbol = fields[0].xpath('node()//text()').extract_first()
            cie['symbol'] = fields[0].xpath('node()//text()').extract_first()
            cie['cie'] = fields[1].xpath('.//text()').extract_first()
            cie['exchange'] = fields[2].xpath('.//text()').extract_first()
            cie['url_smm'] = fields[3].xpath('a/@href').extract_first()
            cie['symbol_cl'] = fields[3].xpath('.//text()').extract_first()
            cie['exchange_cl'] = fields[4].xpath('.//text()').extract_first()
            cie['sector'] = fields[5].xpath('.//text()').extract_first()
            cie['industry'] = fields[6].xpath('.//text()').extract_first()

            cies_dict[symbol] = cie

        jstr = json.dumps(cies_dict, ensure_ascii=False, indent=4)

        with open('../../cies_smm.json', 'w+') as fh:
            fh.write(jstr)



