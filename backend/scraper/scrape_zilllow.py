from bs4 import BeautifulSoup
from zillow_payload import ZillowPayload


def main():
	state_filters = dict(
		filterState=dict(
			price=dict(
				min=100000,
				max=1000000
			),
			beds=dict(min=3),
			baths=dict(min=2)
		)
	)

	zillow_query = ZillowPayload('Austin, TX', state_filters)

	print(zillow_query.get_url())

if __name__ == '__main__':
	main()