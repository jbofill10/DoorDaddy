class ZillowPayload:
	"""
	Used to store the search parameters for a house query
	"""

	# State_filters start as None to indicate no selection
	# setter functions (if they are used) will handle the
	# actual dictionary	structure

	state_filters = dict(
		price=None,
		beds=None,
		baths=None,
		basement=None,
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

	def __init__(self, search_term: str, state_filter: dict, sort_filter: str) -> None:
		pass

	def set_search_term(self, search_term: str) -> None:
		self.search_term = search_term

	def set_state_filters(self, state_filter: dict) -> None:
		pass

	def _set_numeric_state_filters(self, filter_type: str, min, max):
		"""
		Sets numerical filter values like
		price, beds, baths, etc.
			filter_type: The filter to edit
			min: The minimum amount
			max: The maximum amount
		"""

		self.state_filters[filter_type]['min'] = min
		self.state_filters[filter_type]['max'] = max

	def _set_bool_state_filter(self, filter_type: str, val: bool) -> None:
		"""
		Sets filter condition for values such as
		single_family, apartment, etc.
			filter_type: The filter to edit
			val: Boolean value of whether to use it or not
		"""

		self.state_filters[filter_type] = val

