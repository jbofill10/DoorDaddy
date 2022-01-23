import urllib
import json
from warnings import filters

class ZillowPayload:
	"""
	Used to store the search parameters for a house query
	"""

	# State_filters start as None to indicate no selection
	# setter functions (if they are used) will handle the
	# actual dictionary	structure

	ZILLOW_BASE_URL = 'https://www.zillow.com/homes'
	filters = dict(
		filterState=dict()
	)
	# filters = dict(
	# 	usersSearchTerm=None,
	# 	filterState=dict(
	# 		price=None,
	# 		beds=dict(min=None),
	# 		baths=dict(min=None),
	# 		# garage
	# 		gar=dict(value=True),
	# 		# basement finished
	# 		basf=dict(value=True),
	# 		# basement unfinished
	# 		basu=dict(value=True),
	# 		sqft=dict(min=2000, max=5000),
	# 		lot=dict(min=2000, max=5000),
	# 		# parking spots, no clue why zillow calls it "parks"
	# 		parks=dict(value=1),
	# 		# single family home
	# 		sf=dict(value=True),
	# 		# apartment
	# 		apa=dict(value=False),
	# 		# town home
	# 		tow=dict(value=False),
	# 		# multi-family home
	# 		mf=dict(value=False),
	# 		# manufactured home
	# 		manu=dict(value=False),
	# 		# lots or land
	# 		land=dict(value=False)
	# 	)
	# )

	def __init__(self, search_term: str, state_filters: dict, sort_filter: str = '') -> None:

		self.search_term = search_term
		# merge dicts
		self.filters = state_filters

		# Duplicate storage, but makes sense when I dump to JSON, so fuck it
		self.filters['usersSearchTerm'] = self.search_term

		self.sort_filter = sort_filter
		pass

	def update_filter(self, search_term: str, filter: dict) -> None:
		"""
		Updates filters after zillow singleton exists if necessary to update
		"""
		self.filters = filters
		self.search_term = search_term

	def get_url(self) -> str:
		"""
		Prepares url using data held in the payload object
		@returns:
			url string to get html from the query
		"""
		print(self.filters)
		url_without_encoding = f'{self.ZILLOW_BASE_URL}/{self.search_term}_rb/?searchQueryState='
		url_to_encode = urllib.parse.quote(
			json.dumps(
				self.filters,
				separators=(',', ':'))
		)

		return url_without_encoding + url_to_encode
