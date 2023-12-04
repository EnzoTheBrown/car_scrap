import pandas as pd
import asyncio
import boto3
from io import StringIO
from datetime import datetime
from scrapping.cars.aramis import AramisScrapper
from scrapping.cars.autosphere import AutoSphereScrapper
from scrapping.cars.heycar import HeyCarScrapper
from scrapping.cars.autohero import AutoHeroScrapper
from scrapping.cars.lacentrale import LaCentraleScrapper
from scrapping.settings import PROXIES
import uuid

import os

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_default_region = os.getenv("AWS_DEFAULT_REGION")
proxy_index = int(os.getenv("INDEX"))
limit = int(os.getenv("limit"))

SCRAPPERS = [
    AramisScrapper,
    AutoSphereScrapper,
    HeyCarScrapper,
    AutoHeroScrapper,
    LaCentraleScrapper,
]

PROXY = PROXIES[proxy_index]

s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_default_region)

BUCKET_NAME = 'carwatch'


def save_to_s3(df, bucket, key):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())


def run_functions_in_parallel(SCRAPPER):
    scrapper = SCRAPPER(PROXY)
    loop = asyncio.get_event_loop()
    range_ = scrapper.get_range(proxy_index)
    hrefs = loop.run_until_complete(scrapper.extract_hrefs(range_=range(range_[0], range_[1])))
    cars = loop.run_until_complete(scrapper.extract_cars(hrefs))
    return pd.DataFrame(cars)


def load_new_cars():
    df = run_functions_in_parallel(AramisScrapper)
    now = datetime.now().strftime('%Y-%m-%dT%H%M%S')

    save_to_s3(df, BUCKET_NAME, 'aramis' + '-' + now + '-' + str(uuid.uuid4()) + '.csv')


if __name__ == '__main__':
    load_new_cars()
