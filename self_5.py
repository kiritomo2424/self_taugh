#1
musician = []

musician.append("Radwimps")
musician.append("ASIAN KUNG GENERATIONS")
musician.append("ELLE GARDEN")

print(musician)

#2
Pilipunes = (14.3615,120.5855)
America = (40.45,73.59)
Germany = (52.30,13.22)

Country = [Pilipunes,America,Germany]

print(Country)

#3
kirigane = {}

kirigane["height"] = "170"
kirigane["weight"] = "67"
kirigane["name"] = "daisuke"

print(kirigane)

#4
kiri = input("切金の情報を入力して下さい：")


print(kirigane[kiri])

#5
musician_dict = {}

for mus in musician:
    music = input(mus+"の好きな曲を入力して：")
    musician_dict[mus] = music

print(musician_dict)
