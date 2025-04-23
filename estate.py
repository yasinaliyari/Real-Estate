from base import BaseClass
from abc import Abc, abstractmethod

class EstateAbstract(BaseClass):
    def __init__(self, user, area, rooms_count, built_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.rooms_count = rooms_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)


class Apartment(EstateAbstract):
    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)


class House(EstateAbstract):
    def __init__(self, has_yard, floors_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floors_count = floors_count
        super().__init__(*args, **kwargs)