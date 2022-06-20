class Wishlist:
    def __init__(self,items):
        self.items =list(items)

    def __len__(self):
        return len(self.items)
    # lm3rfet 3dd el wishlist

    def __getitem__(self, item):
        return self.items[item]
    # le7dar el 3onsor rqam []

    def __add__(self, other):
        return self.items.append(other)
    # fe 7alet 3aizen ndef 3onzor 2a5r

    def __str__(self):
        wishlist= []
        for index , item in enumerate (self.items):
            wishlist.append(f'{index + 1}.{item}')
            print("Wishlist:")
            print("*"*30)
        return '\n'.join(wishlist)


my_wishlist =Wishlist(['laptop' ,'new car' , 'new mobile'])

#print(len(my_wishlist))
#print(my_wishlist[2])

my_wishlist + 'clothes'
#print(my_wishlist[3])

print(my_wishlist)