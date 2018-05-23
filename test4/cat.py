class cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.mingau_hungry = False
        self.walking_distance = 0

    def miar(self):
        if self.mingau_hungry:
            return 'MIAUUUUUUUUUUUUUUUUUUUUUUuuU'
        return 'Miau, Miau'

    def walk(self):
        """Cat is walking.""""
        self.walking_distance += 1
        self.mingau_hungry = True
        return 'Mingau is walking'

    @property
    def is_old(self):
        """Validade if a cat is old."""
        if self.age > 3:
            return True
        else:
            return False

    @property
    def is_tired(self):
        """Validate if cat is tired."""
        if self.walking_distance > 5:
            return True
        else:
            return False


mingau = cat('Mingau', 'White', 2)

'''
print(mingau.name)
print(mingau.color)
print(mingau.age)
print(mingau.miar())
print(mingau.walk())
print(mingau.miar())

print(mingau.is_old)
print(mingau.is_tired)
print(mingau.walk())
print(mingau.is_tired)
print(mingau.walk())
print(mingau.is_tired)
print(mingau.walk())
print(mingau.is_tired)
print(mingau.walk())
print(mingau.is_tired)
print(mingau.walk())
print(mingau.is_tired)
print(mingau.walk())
print(mingau.is_tired)
print(mingau.walk())
print(mingau.is_tired)
print(mingau.walk())
print(mingau.is_tired)
print(mingau.walk())
'''
