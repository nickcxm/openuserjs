from scrapy.spider import Spider
from openuserjs.items import UserJsItem
from scrapy import Request

class UserjsSpider(Spider):
    name ="userjs"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url="https://openuserjs.org/?p=1"
        yield Request(url,headers=self.headers)

    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response,self)
        item=UserJsItem()
        jss=response.xpath('.//tr[@class="tr-link"]/td')
        for js in jss:
            item['name']=js.xpath('.//a[@class="tr-link-a"]/b/text()').extract();
            print(js.xpath('.//td/a[@class="tr-link-a"]/b/text()'))
            print(item)
            yield item
