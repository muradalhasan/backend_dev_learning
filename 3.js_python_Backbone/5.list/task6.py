str1=input().split(",")
lst=[]
for i in str1:
    lst.append(int(i))
idx=0
num=0
for i in range(len(lst)):
    if lst[i]>num:
        idx=i
        num=lst[i]
print(f"My list:{lst}\nLargest number in the list is {num} which was found at index {idx}")