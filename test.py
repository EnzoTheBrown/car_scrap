from scrapping.cars import generic
from scrapping.cars.aramis import AramisScrapper
from scrapping.cars.autosphere import AutoSphereScrapper
from scrapping.cars.autohero import AutoHeroScrapper
from scrapping.cars.heycar import HeyCarScrapper

from bs4 import BeautifulSoup


class MockDriver:
    page_source = None

    def get(self, file):
        with open(file) as filename:
            self.page_source = filename.read()

    def execute_script(self, *args, **kwargs):
        pass


def test_aramis(monkeypatch):
    monkeypatch.setattr(generic, 'DRIVER', MockDriver())
    scrapper = AramisScrapper()
    scrapper.URL = 'materials/aramis/main.html'
    assert len(scrapper.extract_hrefs(limit=1)) == 1


def test_autohero(monkeypatch):
    monkeypatch.setattr(generic, 'DRIVER', MockDriver())
    scrapper = AutoHeroScrapper()
    scrapper.URL = 'materials/autohero/main.html'
    assert len(scrapper.extract_hrefs(limit=1)) == 1


def test_autosphere(monkeypatch):
    monkeypatch.setattr(generic, 'DRIVER', MockDriver())
    scrapper = AutoSphereScrapper()
    scrapper.URL = 'materials/autosphere/main.html'
    assert len(scrapper.extract_hrefs(limit=1)) == 1


def test_heycar(monkeypatch):
    monkeypatch.setattr(generic, 'DRIVER', MockDriver())
    scrapper = HeyCarScrapper()
    scrapper.urls = {'SUV': 'materials/heycar/main.html'}
    scrapper.suffix = ''
    assert len(scrapper.extract_hrefs(limit=1)) == 1


def test_get_car_aramis(monkeypatch):
    monkeypatch.setattr(generic, 'DRIVER', MockDriver())
    scrapper = AramisScrapper()
    with open('materials/aramis/test1.html') as file:
        soup = BeautifulSoup(file.read(), "html.parser")
    scrapper.extract_car(soup)


def test_get_car_autohero(monkeypatch):
    monkeypatch.setattr(generic, 'DRIVER', MockDriver())
    scrapper = AutoHeroScrapper()
    with open('materials/autohero/test1.html') as file:
        soup = BeautifulSoup(file.read(), "html.parser")
    scrapper.extract_car(soup)


def test_get_car_autosphere(monkeypatch):
    monkeypatch.setattr(generic, 'DRIVER', MockDriver())
    scrapper = AutoSphereScrapper()
    with open('materials/autosphere/test1.html') as file:
        soup = BeautifulSoup(file.read(), "html.parser")
    scrapper.extract_car(soup)


def test_get_car_heycar(monkeypatch):
    monkeypatch.setattr(generic, 'DRIVER', MockDriver())
    scrapper = HeyCarScrapper()
    with open('materials/heycar/test1.html') as file:
        soup = BeautifulSoup(file.read(), "html.parser")
    scrapper.extract_car(soup)
