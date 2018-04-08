from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
from ..models import Sources

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = get_sources()
	return render_template('index.html', sources = sources)