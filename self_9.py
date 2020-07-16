#uft-8
import csv

#1
with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())

#2
answer = input("好きな色は？：")
with open("self_9.txt","w",encoding="utf-8") as a:
    a.write(answer)

#3
list =[ ["Top Gun","Risky Revenant","Minority"],["Trainin Day","Man on Fire","Flight"]]
with open("self_9.csv","w",encoding="utf-8") as c:
    w = csv.writer(c,delimiter=",")
    for i in list:
        w.writerow(i)
print(w)

#4
list = [["トップガン","リスキー","マイノリティ"],["トレインデイ","マン　オブ　ファイヤ","フライト"]]
with open('utf8.csv', 'w', newline='', encoding='utf8') as c:
    w = csv.writer(c,delimiter=",")
    for i in list:
        w.writerow(i)
print(w)
