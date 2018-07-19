from scrapy.spider import Spider
from openuserjs.items import UserJsItem
from scrapy import Request
class UserjsSpider(Spider):
    name ="userjs"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    i=1;
    def start_requests(self):
        url="https://openuserjs.org/?p=1"
        yield Request(url,headers=self.headers)

    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response,self)
        item=UserJsItem()
        jss=response.xpath('//table[@class="table table-hover"]//tbody/tr[@class="tr-link"]')

        for js in jss:
            item['name']=js.xpath('./td[1]/a/b/text()').extract()[0];
            try:
                item['version']=js.xpath('./td[1]/span[@class="script-version label label-default"]/text()').extract()[0]
            except IndexError:
                item['version']="none";
            item['author'] = js.xpath('./td[1]/span[@class="inline-block"]/a/text()').extract()[0];
            try :
                item['desc'] = js.xpath('./td[1]/p/text()').extract()[0]
            except IndexError:
                item['desc']="none";
            item['installs'] = js.xpath('./td[2]/p/text()').extract()[0];
            item['rating'] = js.xpath('./td[3]/p/text()').extract()[0];
            item['updated'] = js.xpath('./td[4]/time/text()').extract()[0];
            # print(item)
            yield item
        i = response.url.split("=")[-1];
        i=int(i);
        i+=1;
        if i<245:
            next_url="https://openuserjs.org/?p="+str(i);
            yield Request(next_url,headers=self.headers)
