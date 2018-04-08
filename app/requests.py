import urllib.request,json
from .models import Sources

#getting the api key
api_key = None

#getting the news base url
base_url = None

def configure_request(app):
	global api_key,base_url
	api_key = app.config['NEWS_API_KEY']
	base_url = app.config['NEWS_SOURCES_BASE_URL']

def get_sources():
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = base_url.format(api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		movie_results = None

		if get_sources_response['results']:
			sources_results_list = get_sources_response['results']
			sources_results = process_results(sources_results_list)

	return movies_results