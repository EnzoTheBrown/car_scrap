from scrapping.cars.heycar import HeyCarScrapper
import pandas as pd

# heycar
df = pd.read_csv('scrapping3.csv')
df = df[df['seller'] == 'heycar']
heycar_scrapper = HeyCarScrapper()
cars = []

for _, row in df.iloc[:5].iterrows():
    try:
        soup = heycar_scrapper.get_soup(row['href'])
        car = heycar_scrapper.extract_car(soup)
        cars.append(car)
    except Exception as e:
        print(e)
        pass

df = pd.DataFrame(cars)
df.to_csv('heycar.csv')

# autosphere
from scrapping.cars.autosphere import AutoSphereScrapper
import pandas as pd

df = pd.read_csv('scrapping3.csv')
df = df[df['seller'] == 'autosphere']
autosphere_scrapper = AutoSphereScrapper()
cars = []

for _, row in df.iterrows():
    try:
        soup = autosphere_scrapper.get_soup(row['href'])
        car = autosphere_scrapper.extract_car(soup)
        cars.append(car)
    except Exception as e:
        print(e)
        pass

df = pd.DataFrame(cars)
df.to_csv('autosphere.csv')


# autohero
from scrapping.cars.autohero import AutoHeroScrapper
import pandas as pd

df = pd.read_csv('scrapping3.csv')
df = df[df['seller'] == 'autohero']
from tqdm import tqdm
autohero_scrapper = AutoHeroScrapper()
cars = []

for _, row in tqdm(df.iterrows()):
    try:
        soup = autohero_scrapper.get_soup(row)
        car = autohero_scrapper.extract_car(soup)
        cars.append(car)
    except:
        pass
df = pd.DataFrame(cars)
df.to_csv('autohero.csv')


# aramis
from scrapping.cars.aramis import AramisScrapper

import pandas as pd
import re

df = pd.read_csv('scrapping3.csv')
df = df[df['seller'] == 'aramis']
aramis_scrapper = AramisScrapper()
cars = []

hrefs = aramis_scrapper.extract_hrefs()

old_hrefs = list(df['href'])
new_hrefs = [href for href in hrefs if href not in old_hrefs]

dd = pd.DataFrame([{'seller': 'aramis', 'href': href} for href in hrefs])

pd.concat([pd.read_csv('scrapping3.csv'), dd]).drop_duplicates().to_csv('scrapping_4.csv')

for href in new_hrefs:
    try:
        soup = aramis_scrapper.get_soup(href)
        aramis_scrapper.vehicule_id = re.findall('vehicleId=(.*)', aramis_scrapper.MAIN_URL + href)[0]
        car = aramis_scrapper.extract_car(soup)
        cars.append(car)
    except Exception as e:
        pass

df = pd.DataFrame(cars)
df.to_csv('aramis2.csv')

