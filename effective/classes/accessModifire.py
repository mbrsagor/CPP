class MyParentObject:
    def __init__(self):
        self.__private_field = 71
        self.public_field = 19


class SubClass(MyParentObject):
    def get_private_field(self):
        try:
            return self.__private_field
        except AttributeError as e:
            return f"Sorry the field is private"
        finally:
            return "Great logic"

    def get_public_field(self):
        return self.public_field


sub_class = SubClass()
print(sub_class.get_private_field())
print(sub_class.get_public_field())
