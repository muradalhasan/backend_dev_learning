lst1=[1, 4, 3, 2, 6]
lst2=[5, 6, 9, 8, 7]
flag=False
for i in lst2:
    if i in lst1:
        flag=True
        break
print(flag)