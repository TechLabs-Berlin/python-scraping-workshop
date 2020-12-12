# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class EbayScraperPipeline:
    def process_item(self, item, spider):

        # if there is no posted_at, skip item
        if item['posted_at'] is '':
            raise DropItem(f"Missing posted_at in {item}")

        # convert PLZ to integer
        item['plz'] = int(item['plz'])

        return item
