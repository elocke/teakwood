from flask import Blueprint, render_template

# from app import models
# from ..models import Artist

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return render_template('main.html')
