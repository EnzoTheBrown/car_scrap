from abc import ABC, abstractmethod


class GenericCar(ABC):
    def __init__(self, soup, vehicule_id=None):
        self.soup = soup
        self.vehicule_id = vehicule_id

    @staticmethod
    def parse_int(token):
        try:
            return int(''.join(i for i in token if i.isdigit()))
        except:
            pass

    @staticmethod
    def parse_date(date):
        try:
            return int(date[-4:])
        except:
            pass
        
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def leasing(self):
        pass

    @abstractmethod
    def equipments(self):
        pass

    @abstractmethod
    def date(self):
        pass

    @abstractmethod
    def motor(self):
        pass

    @abstractmethod
    def fuel(self):
        pass

    @abstractmethod
    def transmission(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def kilometers(self):
        pass

    @abstractmethod
    def doors(self):
        pass

    @abstractmethod
    def seats(self):
        pass

    @abstractmethod
    def images(self):
        pass

    @abstractmethod
    def defauts(self):
        pass

    @abstractmethod
    def location(self):
        pass

    def critair(self):
        pass

    def extra(self):
        return {}

    def to_json(self):
        return {
            'name': self.name(),
            'price': self.parse_int(self.price()),
            'leasing': self.parse_int(self.leasing()),
            'equipments': self.equipments(),
            'date': self.parse_date(self.date()),
            'motor': self.motor(),
            'fuel': self.fuel(),
            'transmission': self.transmission(),
            'type': self.type(),
            'kilometers': self.parse_int(self.kilometers()),
            'doors': self.parse_int(self.doors()),
            'seats': self.parse_int(self.seats()),
            'images': self.images(),
            'defauts': self.defauts(),
            'location': self.location(),
            'critair': self.critair(),
            'extra': self.extra(),
        }