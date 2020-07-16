a = "good"
b = "not bad"
c = "bad"

print(a)
print(b)
print(c)

x = 11

if x < 10:
    print(a)
else:
    print(b)

if x <= 10:
    print(a)
elif x > 10 and x <= 25:
    print(b)
else:
    print(c)

y = 23

print(y % x)
print(y // x)

age = -29

if age < 20:
    print("you are yung")
elif age <30:
    print("you are yung yet!")
else:
    print("you are good age")
