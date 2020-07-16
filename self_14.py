x = 10

if x is None:
    print("xはNone　:(")
else:
    print("xはNoneじゃない")


x=None
if x is None:
    print("xはNone　:(")
else:
    print("xはNoneじゃない")

#1
class Square:
    square_list = []
    def __init__(self,l):
        self.len = l
        self. square_list.append(self.len)

    def __repr__(self):
        return "{}by{}".format(self.len,self.len)

s1 = Square(10)
s2 = Square(29)
s3 = Square(15.5)

print(Square.square_list)
print(s1.square_list)
print(s2.square_list)
print(s3.square_list)

#2
print(s1)
print(s2)
print(s3)

def same(a,b):
    if a is b:
        return True
    else:
        return False

print(same(4,4))
print(same("v","v"))
print(same(s1,s2))
print(same(s1,s1))
