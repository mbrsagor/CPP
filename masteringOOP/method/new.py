class FloatUnits(float):
    def __new__(cls, value, unit):
        obj = super().__new__(cls, value)
        obj.unit = unit
        return obj


speed = FloatUnits(5.9, 'kg')
print(f"{speed} {speed.unit}")


class Unit:
    """Full name for the unit."""
    factor = 1.0
    standard = None
    name = ""

    @classmethod
    def value(cls, value):
        if value is None: return None
        return value / cls.factor

    @classmethod
    def convert(cls, value):
        if value is None: return None


class UnitMeta(type):
    def __new__(cls, name, base, dict):
        new_class = super().__new__(cls, name, base, dict)
        new_class.standard = new_class
        return new_class
