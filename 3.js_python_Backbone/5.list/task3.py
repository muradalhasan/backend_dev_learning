lst=[]
for i in range(5):
    n=int(input("Enter a number: "))
    lst.append(n)
for i in range(len(lst)-1, -1, -1):
    print(lst[i])
