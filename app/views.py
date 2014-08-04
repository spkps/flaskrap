# coding=utf-8

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for

import forms

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
