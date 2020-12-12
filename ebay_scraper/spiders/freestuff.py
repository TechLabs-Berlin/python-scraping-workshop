import scrapy


class FreestuffSpider(scrapy.Spider):
    name = 'freestuff'
    allowed_domains = ['ebay-kleinanzeigen.de']
    start_urls = ['https://www.ebay-kleinanzeigen.de/s-zu-verschenken/berlin/c192l3331']

    def parse(self, response):

        # extracting the content using selectors
        ads = response.css('article.aditem')
        for ad in ads:
            ad_id = ad.xpath('@data-adid').get()
            image = ad.css('.aditem-image div').xpath('@data-imgsrc').get()
            title = ad.css('.aditem-main h2 a::text').get()
            description = ad.css('.aditem-main p::text')[0].get()
            location = ads.css('.aditem-details::text').getall()
            plz = location[0]
            district = location[1]
            posted_at = ad.css('.aditem-addon::text').get()

            ad_item = {
                'ad_id': ad_id,
                'image': image,
                'title': title,
                'description': description,
                'plz': plz.strip(),
                'district': district.strip(),
                'posted_at': posted_at.strip()
            }

            yield ad_item

