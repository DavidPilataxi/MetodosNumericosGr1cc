
import scrapy

class PythonNewsSpider(scrapy.Spider):
    name = "python_news"
    start_urls = ['https://www.python.org/blogs/']

    def parse(self, response):
        for article in response.css('h2.entry-title'):
            yield {
                'Título': article.css('a::text').get(),
                'Enlace': article.css('a::attr(href)').get(),
            }
