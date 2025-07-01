from sample import create_sample
from advertisment import ApartmentSell, HouseSell, ApartmentRent, HouseRent

class Handler:
    def run(self):
        print('hello world')

if __name__ == "__main__":
    create_sample()
    handler = Handler()
    
    handler.run()