from flask import Blueprint, render_template

# from app import models
from ..models import Artist

main = Blueprint('main', __name__, template_folder='pages')

@main.route('/')
def index():
	artists = Artist.objects[40:50]
	# for i in artists:
	# 	print i    
	return render_template('main/main.html', artists=artists)

@main.route('/<artist_name>')
def browse_albums(artist_name):
	artists = Artist.objects().filter(name=artist_name).order_by('-date').all()
	# for i in artists:
	# 	print i.name
	# 	print dir(i)
	# 	print dir(i.shows)
	# 	for k in i.shows:
	# 		print k.title 
	# 		print k.location
	# 		print k.venue
	# 		print k.date
	# 		print k.description
	# 		for f in k.files:
	# 			print f
	return render_template('main/artist.html', artists=artists)


