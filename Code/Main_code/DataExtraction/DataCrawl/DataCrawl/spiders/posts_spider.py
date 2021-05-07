import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://www.cascades.com/sites/default/files/Investor/Trimestre/T1-2020-Quarterly-report.pdf'
    ]

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header h2 a::text')[0].extractText(),
                'date': post.css('.post-header a::text')[1].extractText(),
                'author': post.css('.post-header a::text')[2].extractText()
            }
        next_page = response.css('a.next-posts-link::attr(href)').extractText()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

