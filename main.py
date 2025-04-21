from user import User
from random import choice

First_Name = ['yasin', 'Ali', 'Mehdi']
Last_Name = ['Aliyari', 'Miri', 'Ajam']
Mobiles = ['09123456789', '09876543219', '09625438756', '09621872988']

if __name__ == "__main__":
    for mobile in Mobiles:
        User(choice(First_Name), choice(Last_Name), mobile)

    for user in User.objects_list:
        print(f"{user.id}\t {user.fullname}")