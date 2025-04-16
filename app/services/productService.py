from amazon_paapi import AmazonApi
from flask import jsonify
import os


class ProductService:
    def __init__(self):
        self.__key = os.environ.get('KEY')
        self.__secret = os.environ.get('SECRET')
        self.__partner_tag = os.environ.get('PARTNER_TAG')
        self.__country = "ES"
        self.amazon = AmazonApi(
            key=self.__key,
            secret=self.__secret,
            tag=self.__partner_tag,
            country=self.__country
        )

    def search(self, query):
        products = self.amazon.search_items(keywords="hidratacion piel grasosa", search_index="Beauty", item_count=10)
        products_info = []
        for item in products.items:
            products_info.append({
                'name': item.item_info.title.display_value,
                'url': item.detail_page_url,
                'img_url': item.images.primary.large.url,
                'review': item.customer_reviews,
                'price': item.offers.listings[0].price.amount,
                'brand': item.item_info.by_line_info.brand.display_value
            })
            try:
                products_info[-1]['features'] = item.item_info.features.display_values
            except AttributeError:
                products_info[-1]['features'] = []

        return products_info

