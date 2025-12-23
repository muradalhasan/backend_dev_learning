tup=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
inp=int(input())
count=0
for i in tup:
    if i==inp:
        count+=1
print(f"{inp} appears {count} times in the tuple")