from user import User
from random import choice
from region import Region
from estate import Apartment, House, Store
from advertisment import ApartmentSell, HouseSell, ApartmentRent, HouseRent

First_Name = ['yasin', 'Ali', 'Mehdi']
Last_Name = ['Aliyari', 'Miri', 'Ajam']
Mobiles = ['09123456789', '09876543219', '09625438756', '09621872988']

if __name__ == "__main__":
    for mobile in Mobiles:
        User(choice(First_Name), choice(Last_Name), mobile)

    for user in User.objects_list:
        print(f"{user.id}\t {user.fullname}")


    reg1 = Region(name='R-one')
    reg2 = Region(name='R-two')
    reg3 = Region(name='R-three')

    apt1 = Apartment(
        has_elevator=False,
        has_parking=True,
        floor=3,
        user=User.objects_list[1],
        region=reg1,
        built_year=1398,
        area=100,
        rooms_count=3,
        address='shahrood'
    )
    
    # apt1.show_description()


    hou1 = House(
        has_yard=True,
        floors_count=2,
        user=User.objects_list[0],
        area=400,
        rooms_count=4,
        built_year=1403,
        region=reg2,
        address='shahrood'
    )

    # hou1.show_description()


    str1 = Store(
        user=User.objects_list[2],
        area=50,
        built_year=1390,
        region=reg1,
        rooms_count=0,
        address='tehran'
    )

    # str1.show_description()


    aptsl1 = ApartmentSell(
        has_elevator=True,
        has_parking=True,
        floor=1,
        user=User.objects_list[1],
        built_year=1395,
        region=reg2,
        area=400,
        rooms_count=4,
        convertable=False,
        address='isfahan',
        price_per_meter=500,
        discountable=True
    )


    aptsl1.show_detail()



    housl1 = HouseSell(
        has_yard=True,
        floors_count=1,
        user=User.objects_list[0],
        area=500,
        rooms_count=5,
        built_year=1402,
        region=reg2,
        address='tehran',
        price_per_meter=100,
        discountable=False,
        convertable=False
    )

    housl1.show_detail()


    aptrt1 = ApartmentRent(
        has_elevator=True,
        has_parking=False,
        floor=5,
        user=User.objects_list[0],
        area=150,
        rooms_count=3,
        built_year=1404,
        region=reg3,
        address='shahrood',
        initial_price=120,
        monthly_price=5
        )
    

    housrt1 = HouseRent(
        has_yard=True,
        floors_count=1,
        user=User.objects_list[2],
        area=300,
        rooms_count=4,
        built_year=1400,
        region=reg1,
        address='tehran',
        initial_price=500,
        monthly_price=20
    )


    print(ApartmentSell.manager)
    print(ApartmentRent.manager)
    print(HouseSell.manager)
    print(HouseRent.manager)