from flask import Blueprint, render_template

# from app import models
# from ..models import Artist

partials = Blueprint('partials', __name__)

# @partials.route('/<partial>')
# def partial(partial):
# 	return render_template(partial,jinja_var='this is from jinja')

@partials.route('/<path:path>')
def serve_partial(path):
    return render_template('/partials/{}'.format(path))