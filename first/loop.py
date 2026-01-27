fruits = ["Apple","Banana","Kiwi"]
i = 1
j = 1
k = 1
for x in fruits:
    print(f"{i}.",x,)
    i+=1

for x in fruits:
    print(f"{j}.",x,)
    j+=1
    if x=="Banana":
        break
    
for x in fruits:
    if x=="Banana":
        continue
    print(f"{k}.",x,)
    k+=1
    