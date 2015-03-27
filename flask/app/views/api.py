from flask import Blueprint, render_template
import jsonify 
# from app import models
# from ..models import Artist

api = Blueprint('api', __name__)

@api.route('/')
def index():
	# artists = Artist.objects[40:50]
	# for i in artists:
	# 	print i    
	return render_template('main/main.html')

@api.route('/artists)
def list_artists(artist_name):
	# artists = Artist.objects[40:50]
	# for i in artists:
	# 	print i    

	
	return jsonify(results)


@api.route('/artists/<artist_name>')
def list_artist(artist_name):
	# artists = Artist.objects[40:50]
	# for i in artists:
	# 	print i    

	
	return jsonify(results)


@api.route('/shows/<artist_name>/')
def list_shows(artist_name):
	# artists = Artist.objects[40:50]
	# for i in artists:
	# 	print i    

	
	return jsonify(results)

@api.route('/shows/<artist_name>/<show_date>')
def list_show(artist_name, show_date):
	# artists = Artist.objects[40:50]
	# for i in artists:
	# 	print i    

	
	return jsonify(results)

