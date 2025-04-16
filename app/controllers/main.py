from flask import render_template
from app.services.productService import ProductService


class MainController:

    def __init__(self):
        self.product = ProductService()

    def details(self):
        products = self.product.search(query='cremas antiarrugas')
        return render_template('main/details.html', products=products)

