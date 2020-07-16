#1
movies = ["ウォーキンデッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイナリーズ"]

for movie in movies:
    print(movie)

#2
for i in range(25,51):
    print(i)

#3
for n,movie in enumerate(movies):
    print(n)
    print(movie)


#4
numbers = [3,1,5,7,3,4,9]
i = 0
while  True:
    a = input("数字 or q")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("please type a number or q to quit.")
    if a in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")

#5
list1 = [8,19,148,4]
list2 = [9,1,33,83]
list_mul = []

for l1 in list1:
    for l2 in list2:
        list_mul.append(l1*l2)
print(list_mul)
