from flask import Blueprint, render_template

# from app import models
# from ..models import Artist

main = Blueprint('main', __name__)

@main.route('/')
def index():
	# artists = Artist.objects[40:50]
	# for i in artists:
	# 	print i    
	return render_template('main/main.html')
