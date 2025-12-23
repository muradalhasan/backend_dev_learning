str1=input().split(",")

new=[]
for i in str1:
    new.append(int(i))
new1=[]
for i in new:
    if i not in new1:
        new1.append(i)
print(f"Input list: {new}\n Modified List: {new1}")
