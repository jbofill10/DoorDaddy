from enum import Enum

class Filter(Enum):
	PRICE = 'price',
	BEDS = 'beds',
	BATHS = 'baths',
	BASEMENT = 'basement',
	SQFT = 'sqft',
	LOT_SIZE = 'lot_size',
	PARKING_SPOTS = 'parking_spots',
	SINGLE_FAMILY = 'single_family',
	APARTMENT = 'apartment',
	TOWN_HOUSE = 'town_house',
	MULTI_FAMILY = 'multi_family',
	MANUFACTURED = 'manufactured',
	LOTS_OR_LAND = 'lots_or_land'