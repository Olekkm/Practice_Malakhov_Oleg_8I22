import scrapy


class SteamparsSpider(scrapy.Spider):
    name = "SteamPars"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/search/?filter=topsellers?query&start=-100&count=50"]

    def parse(self, response):
        for i in range(999, -1, -50):
            url = "https://store.steampowered.com/search/?filter=topsellers?query&start={}&count=50".format(i)
            yield scrapy.Request(url, callback=self.parse,
                                 cookies={"lastagecheckage": "1-0-1993", "birthtime": "723150001"})
        for a in response.xpath('//div[@id="tabletGrid"]'):
            yield {"name": a.xpath('//div[@id="appHubAppName"]/text()').get(),
                   "tags": list(map(str.strip, a.xpath('//a[@class="app_tag"]/text()').getall()))}
        for a in response.xpath('//div[@id="search_resultsRows"]/a/@href'):
            yield scrapy.Request(a.get(), callback=self.parse,
                                 cookies={"lastagecheckage": "1-0-1993", "birthtime": "723150001"})


if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings={
        'FEEDS': {'steam pars.csv': {'format': 'csv'}},
        'LOG_ENABLED': True

    })

    process.crawl(SteamparsSpider)
    process.start()
