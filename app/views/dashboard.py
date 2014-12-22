from flask import Blueprint, render_template

# from app import models
from ..models import Artist

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/')
def home():
    artists = Artist.objects.all()
    for i in artists:
    	print i    
    return render_template('dashboard/test.html', artists=artists)

@dashboard.route('/<artist_name>')
def browse_albums(artist_name):
    artists = Artist.objects().filter(name=artist_name).all()
    for i in artists:
    	print i.name
    	for k in i.shows:
			print k.title 
		 	print k.location
		 	print k.venue
		 	print k.date
		 	print k.description
    return render_template('dashboard/albums.html', artists=artists)


