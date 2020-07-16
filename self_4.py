def f1():
    a = input("type number")
    a = int(a)
    print(a**2)

f1()

def f2():
    a = input("type strings")
    print(a)

f2()

def f3(a,b,c,d=2,e=3):
    """
    Return a+b+c+d+e.
    :param a:int.
    :param b:int.
    :param c:int.
    """
    print(a+b+c+d+e)

f3(1,2,3)

def f4_1(a):
    return int(a/2)

def f4_2(a):
    return int(a*4)

x = f4_1(5)
print(f4_2(x))

def f5(a):
    try:
         a = float(a)
         print(a)
    except ValueError:
        print("それ数字じゃない")

f5("try!")
