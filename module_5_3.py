#Домашняя работа по уроку "Перегрузка операторов."
class House:
    def __init__(self, name , number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name} , кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return True
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)












h1 = House('Адмирал',26)
h2 = House('Паруса', 33)

print(h1)
print(h2)
print(h1.__len__())
print(h2.__len__())
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
h1 = h1 + 5
print(h1)
print(h1 == h2)
h1+= 10
print(h1)
h2 = 1 + h2
print(h2)
