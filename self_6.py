#1
camu = "カミュ"

for x in "カミュ":
    print(x)

#2
n1 = input("誰が：")
n2 = input("何した：")

words = "{}が{}".format(n1,n2)
print(words)

#3
print("aldous Huxley was born in 1894".capitalize())

#4
w = "どこで？ 誰が？ いつ？"
w_list = w.split(" ")
print(w_list)

#5
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)

#6
print("A screamig comes across the sky".replace("s","$"))

#7
index = "Hemingway".index("m")
print(index)

#8
quote1 = "'Drink up,' said Ford, 'you've got three pints to get through.'"
quote2 = "'I forgot,' Lennie said softly. 'I tried not to forget. Honest to God I did, George.'"
quote3 = "'Yes,' I said, 'I have a reason,' and added very softly, 'My God.'"

#9
print("Three"+" "+"Three"+" "+"Three")

#10
z = "四月の晴れた寒い日で、時計がどれも13時を売っていた。"
z_index = z.index("、")
print(z[:z_index])
