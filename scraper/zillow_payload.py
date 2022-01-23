import urllib
import json

class ZillowPayload:
	"""
	Used to store the search parameters for a house query
	"""

	# State_filters start as None to indicate no selection
	# setter functions (if they are used) will handle the
	# actual dictionary	structure

	ZILLOW_BASE_URL = 'https://www.zillow.com/homes'

	filters = dict(
		usersSearchTerm=None,
		filterState=dict(
			price=None,
			beds=None,
			baths=None,
			# garage
			gar=dict(value=None)
			# basement finished
			basf=dict(value=None),
			# basement unfinished
			basu=dict(value=None)
			sqft=None,
			lot_size=None,
			parking_spots=None,
			single_family=False,
			apartment=False,
			town_house=False,
			multi_family=False,
			manufactured=False,
			lots_or_land=False,
		)
	)

	def __init__(self, search_term: str, state_filters: dict, sort_filter: str = '') -> None:
		self.search_term = search_term
		self.state_filters = state_filters

		# Duplicate storage, but makes sense when I dump to JSON, so fuck it
		self.state_filters['usersSearchTerm'] = self.search_term

		self.sort_filter = sort_filter
		pass

	def set_search_term(self, search_term: str) -> None:
		self.search_term = search_term

	def set_state_filters(self, state_filter: dict) -> None:
		pass

	def get_url(self) -> str:
		"""
		Prepares url using data held in the payload object
		@returns:
			url string to get html from the query
		"""
		url_without_encoding = f'{self.ZILLOW_BASE_URL}/{self.search_term}_rb/?searchQueryState='
		url_to_encode = urllib.parse.quote(
			json.dumps(
				self.state_filters,
				separators=(',', ':'))
		)

		return url_without_encoding + url_to_encode
