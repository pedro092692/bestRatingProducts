from flask import Blueprint, render_template
mainBp = Blueprint('main', __name__)


@mainBp.route('/', methods=['GET'])
def home():
    return render_template('main/index.html');