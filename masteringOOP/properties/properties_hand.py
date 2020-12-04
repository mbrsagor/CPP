# class Hand:
#     def __str__(self):
#         return " ".join(map(str, self.card))
#
#     def __repr__(self):
#         return "{__class__.__name__}({dealer_card!r}, {_cards_str})"
#
#


class Property:

    def __init__(self, var):
        self.a = var

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2


obj = Property(23)
print(obj.a)
