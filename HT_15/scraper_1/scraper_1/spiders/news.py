import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class NewsSpider(CrawlSpider):
    name = "all_news"
    start_urls = ["https://www.vikka.ua/category/novini/"]

    rules = (
        Rule(LinkExtractor(allow='novini/'), callback='parse', follow=True),
    )

    def parse(self, response):
        str_date = ""
        day, month, year = 0, 0, 0
        date_datetime_format, check_date = None, False
        date = input("Ваша дата у форматі yyyy-mm-dd: ")
        print(date)
        dict_of_moths = {"1": "Січня", "2": "Лютого", "3": "Березеня", "4": "Квітеня", "5": "Травня", "6": "Червня",
                         "7": "Липня", "8": "Серпня", "9": "Вересня", "10": "Жовтня", "11": "Листопада", "12": "Грудня"}
        try:
            date_datetime_format = datetime.datetime.strptime(date, "%Y-%m-%d")
            day = date_datetime_format.day
            month = date_datetime_format.month
            month = dict_of_moths[str(month)]
            year = date_datetime_format.year
            str_date = str(day) + " " + month + " " + str(year)
            check_date = True
        except:
            print("Невірна дата")
            NewsSpider.parse(self, response)

        if date_datetime_format.strftime("%Y%m%d") > datetime.datetime.now().strftime("%Y%m%d"):
            check_date = False

        if check_date is True:
            date = str(response.xpath("//span[@class='post-info-style']/text()").extract()).split()
            date_from_web = str(date[0]) + " " + str(date[1]) + " " + str(date[2])
            print(str_date, date_from_web)
            if str_date == date_from_web:
                yield {
                    "title": response.xpath("//h1[@class='post-title -margin-b']/text()").extract(),
                    "news_text": response.xpath("//div[@class='entry-content -margin-b']//p/text()").extract(),
                    "tags": response.xpath("//div[@class='entry-content -margin-b']//p/text()").extract(),
                    "date": response.xpath("//span[@class='post-info-style']/text()").extract()
                }
            if day == int(date[0])-1 and month == date[1] and year == int(date[2]):
                print("Завершено роботу")
                raise SystemExit
        else:
            print("Невірна дата")
            NewsSpider.parse(self, response)
