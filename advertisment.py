from estate import Apartment, House, Store
from deal import Sell, Rent
from base import BaseClass


class ApartmentSell(BaseClass, Apartment, Sell):
    def show_detail(self):
        self.show_description()
        self.show_price()


class ApartmentRent(BaseClass, Apartment, Rent):
    pass


class HouseSell(BaseClass, House, Sell):
    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseRent(BaseClass, House, Rent):
    pass


class StoreSell(BaseClass, Store, Sell):
    pass


class StoreRent(BaseClass, Store, Rent):
    pass