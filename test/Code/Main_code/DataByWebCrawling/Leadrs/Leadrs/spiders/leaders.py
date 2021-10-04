import scrapy


class LeaderSpider(scrapy.Spider):
    name = 'leader'
    start_urls = ['https://www.cascades.com/en/about-us/our-leaders']

    def parse(self, response):
        for leaders in response.css('div.tile'):
            yield {
                'name':leaders.css('h4.heading-regular.px-3::text').get() ,
                'position':leaders.css('p.text-small.px-3').get(),
                'link':response.css('a.link.link--small-arrow.w-auto').get()
            }
