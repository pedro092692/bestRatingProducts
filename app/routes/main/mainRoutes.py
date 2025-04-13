from flask import Blueprint, render_template
from app.controllers.main import MainController
mainBp = Blueprint('main', __name__)

products = MainController()


@mainBp.route('/', methods=['GET'])
def home():
    return render_template('main/index.html')


@mainBp.route('/details', methods=['GET'])
def details():
    return products.details()

