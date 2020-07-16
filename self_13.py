#1
class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self,w,h):
        self.widht = w
        self.height = h

    def calculate_perimeter(self):
        return self.widht * self.height

    def change_size(self,w_change,h_change):
        self.widht_change = w_change
        self.height_change = h_change
        self.widht =self.widht-self.widht_change
        self.height = self.height-self.height_change

class Square(Shape):
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * self.side

rec = Rectangle(2,3)
print(rec.calculate_perimeter())

squ = Square(3)
print(squ.calculate_perimeter())

#2
rec_c = Rectangle(5,5)
print("{}and{}".format(rec_c.widht,rec_c.height))
rec_c.change_size(2,-2)
print("{}and{}".format(rec_c.widht,rec_c.height))

#4
class Horse:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self,name):
        self.name = name

rider = Rider("tomo")
horse = Horse("onozo",rider)
print(horse.owner.name)

#3


rec2 = Rectangle(3,4)
print(rec2.what_am_i())
print(rec2.calculate_perimeter())

squ2 = Square(3)
print(squ2.what_am_i())
print(squ2.calculate_perimeter())
