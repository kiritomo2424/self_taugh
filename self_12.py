class Orange:
    def __init__(self,w,c):
        """weight(重さ)はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self,days,temp):
        """temp(温度)は摂氏"""
        self.mold = days * temp

class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self,w,l):
        self.widht = w
        self.len = l

#1
class Apple:
    def __init__(self,w,c,l,p):
        self.weight = w
        self.color = c
        """localは産地"""
        self.local = l
        """priceは「円」"""
        self.price = p

#2
class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius**2 * math.pi

import math
circle = Circle(2)
print(circle.area())

#3
class Triangle:
    def __init__(self,l_w,h):
        self.low_width = l_w
        self.height = h

    def area(self):
        return self.low_width * self.height / 2

triangle = Triangle(2,3)
print(triangle.area())

#4
class Hexagon:
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side *6

hexagon = Hexagon(3)
print(hexagon.calculate_perimeter())
