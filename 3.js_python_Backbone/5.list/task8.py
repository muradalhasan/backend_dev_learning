lst1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2=[10, 11, 12, -13, -14, -15, -16]
lst=[]
for i in lst1:
    if i%2==0:
        lst.append(i)
for i in lst2:
    if i%2==0:
        lst.append(i)
print(lst)