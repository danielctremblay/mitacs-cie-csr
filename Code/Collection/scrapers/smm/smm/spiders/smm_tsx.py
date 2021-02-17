import json
import scrapy
import logging

logger = logging.getLogger(__name__)

class SmmTsxSpider(scrapy.Spider):
    name = 'smm_tsx'
    allowed_domains = ['stockmarketmba.com']
    start_urls = ['https://stockmarketmba.com/listofstocksforanexchange.php?s=CT']

    def parse(self, response):

        # Parsing Canadian companies
        cies = response.xpath('//table[@id="ETFs"]/tbody/tr')

        cies_dict = {}

        for cie_tree in cies:
            fields = cie_tree.xpath('td')
            cie = {}
            cie['url'] =  fields[0].xpath('a/@href').extract_first()
            cie['symbol_cl'] = fields[0].xpath('node()//text()').extract_first()
            symbol = cie['symbol_cl']
            cie['cie'] = fields[1].xpath('.//text()').extract_first()
            cie['symbol'] = fields[2].xpath('node()//text()').extract_first()
            cie['date_ipo'] = fields[3].xpath('.//text()').extract_first()
            cie['category1'] = fields[4].xpath('.//text()').extract_first()
            cie['category2'] = fields[5].xpath('.//text()').extract_first()
            cie['category3'] = fields[6].xpath('.//text()').extract_first()
            cie['sector'] = fields[7].xpath('.//text()').extract_first()
            cie['isin'] = fields[8].xpath('.//text()').extract_first()
            cie['sedol'] = fields[8].xpath('.//text()').extract_first()

            cies_dict[symbol] = cie

        jstr = json.dumps(cies_dict, ensure_ascii=False, indent=4)

        with open('../../cies_smm_tsx.json', 'w+') as fh:
            fh.write(jstr)



