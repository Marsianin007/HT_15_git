import scrapy
import datetime




class MySpider1Spider(scrapy.Spider):
    date = input("Ваша дата у форматі yyyy-mm-dd: ")
    correct_date = None
    date_datetime_format = None
    try:
        date_datetime_format = datetime.datetime.strptime(date, "%Y-%m-%d")
        day_start = date_datetime_format.day
        month_start = date_datetime_format.month
        year_start = date_datetime_format.year
        correct_date = True
    except:
        print("Невірна дата")


    name = 'my_spider_1'
    allowed_domains = ['https://www.vikka.ua']
    start_urls = ['https://www.vikka.ua/category/novini/']

    def parse(self, response):
        date = response.xpath("//span[@class='post-info-style']/text()").extract()
        title = response.xpath("//h1[@class='post-title -margin-b']/text()").extract()
        news_text = response.xpath("//div[@class='entry-content -margin-b']//p/text()").extract()
        tags = response.xpath("//a[@class='post-tag']/text()").extract()
        #news_url = response.xpath("")

        #for item in zip(title, news_text, news_url):
        #    data_dict = {
        #        "title" : item[0],
        #        "news_text" : item[1],
        #        "news_url" : item[2]
        #    }
        #    yield data_dict







