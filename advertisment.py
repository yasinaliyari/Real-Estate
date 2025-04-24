from estate import Apartment, House, Store
from deal import Sell, Rent


class ApartmentSell(Apartment, Sell):
    pass


class ApartmentRent(Apartment, Rent):
    pass


class HouseSell(House, Sell):
    pass


class HouseRent(House, Rent):
    pass


class StoreSell(Store, Sell):
    pass


class StoreRent(Store, Rent):
    pass