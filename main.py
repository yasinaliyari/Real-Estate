from sample import create_sample
from advertisment import ApartmentSell, HouseSell, ApartmentRent, HouseRent, StoreRent, StoreSell

class Handler:
    ADVERTISMENT_TYPE = {
        1: ApartmentSell, 2: ApartmentRent,
        2: HouseSell, 3: HouseRent,
        4: StoreSell, 5: StoreRent
    }

    def run(self):
        print('hello world')

if __name__ == "__main__":
    create_sample()
    handler = Handler()
    
    handler.run()