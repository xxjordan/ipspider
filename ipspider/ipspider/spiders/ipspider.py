import json
import time

import scrapy
from scrapy import Request

from ipspider.check_ip_able import validateIp
from ipspider.items import IpspiderItem


class ipspider(scrapy.Spider):
    name = 'ipspider'
    sixsixip_url = 'http://www.66ip.cn/{page}'
    xigua_url = 'http://www.xicidaili.com/{page}'
    user_info_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&containerid=100505{uid}'
    followers_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}'
    follow_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&lfid=107603{uid}'
    start_user_id = '5055034462'

    def start_requests(self):

        yield Request(self.sixsixip_url.format(page='index.html'), callback=self.six_ip_spider)
        yield Request(self.xigua_url.format(page='nn/1'), callback=self.xigua_spider)

    def six_ip_spider(self, response):
        item = IpspiderItem()
        page = response.xpath('//*[@id="PageList"]/a')[-1]
        next_page = page.xpath('./@href').extract()[0]

        tbody = response.xpath('///tr')[2:]

        for tr in tbody:
            item['host'] = tr.xpath('./td[1]/text()').extract()[0]
            item['port'] = tr.xpath('./td[2]/text()').extract()[0]
            msg = validateIp(host=item['host'], port=item['port'])
            if msg == 200:
                print(item,1)
                yield item

        yield Request(self.sixsixip_url.format(page=next_page), callback=self.six_ip_spider)

    def xigua_spider(self, response):
        item = IpspiderItem()
        page = response.xpath('//*[@id="body"]/div[2]/a[@class="next_page"]/@href').extract()[0]
        res = response.xpath('//tr')[1:]
        for tr in res:
            item['host'] = tr.xpath('./td[2]/text()').extract()[0]
            item['port'] = tr.xpath('./td[3]/text()').extract()[0]
            msg = validateIp(host=item['host'], port=item['port'])
            if msg == 200:
                print(item,1)
                yield item
        yield Request(self.xigua_url.format(page=page), callback=self.xigua_spider)




