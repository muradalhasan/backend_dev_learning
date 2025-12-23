str1=input()
flag=True
for i in str1:
    if i!="0" and i!="1":
        flag=False
        break
if flag:
    print("Binary Number")
else:
    print("Not a binary number")

