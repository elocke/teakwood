from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
# import logging

bp = Blueprint('frontend', __name__, template_folder='templates', static_folder='static')

@bp.route('/')
def indexbp():
	# logging.error('loaded frontend')
	return render_template('app_base.html')

# @bp.route('/<path:path>')
# def static_proxy(path):
#   # send_static_file will guess the correct MIME type
#   print path
#   print bp.send_static_file(path)
#   return bp.send_static_file(path)
