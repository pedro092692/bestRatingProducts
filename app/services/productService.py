import amazon_paapi.errors
from amazon_paapi import AmazonApi
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
        products = self.amazon.search_items(keywords='harry potter')

        print(products)

