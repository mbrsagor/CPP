class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


class_method = Demo.klassmeth('spam')
print(class_method)

static_method = Demo.statmeth('spam')
print(static_method)
