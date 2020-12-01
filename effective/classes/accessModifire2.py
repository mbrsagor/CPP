class MyBaseClass(object):

    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


my_base_class = MyBaseClass("sagor")
print(my_base_class.get_value())


class MyStringClass(MyBaseClass):
    def get_value(self):
        return str(super(MyStringClass, self).get_value())  # Update


my_str_class = MyStringClass('Second class')
print(my_str_class.get_value())


class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)  # Not updated


foo = MyIntegerSubclass(5)
# print(foo.get_value())
