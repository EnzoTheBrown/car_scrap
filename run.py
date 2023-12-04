from scrapping.cars.lacentrale import LaCentraleScrapper
from scrapping.settings import PROXIES
import asyncio

proxy = PROXIES[1]
la_centrale_scrapper = LaCentraleScrapper(proxy)
la_centrale_scrapper.get_range(2)

loop = asyncio.get_event_loop()
range_ = la_centrale_scrapper.get_range(1)
hrefs = loop.run_until_complete(la_centrale_scrapper.extract_hrefs(range_=range(range_[0], range_[1])))
cars = loop.run_until_complete(la_centrale_scrapper.extract_cars(hrefs))
