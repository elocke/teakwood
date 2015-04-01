from flask import Blueprint, render_template
import logging
# from app import models
# from ..models import Artist

main = Blueprint('main', __name__)

@main.route('/')
def index():
	logging.error('loaded main')
	return render_template('main.html')
