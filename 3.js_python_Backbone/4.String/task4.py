str1=input("Enter a string: ")
new=''
flag=True
if len(str1)>3:
    if str1[-3:]=="est":
        flag=False
    if str1[-2:]=="er":
        if flag:
            new=str1[:-2]+"est"
            print(new)
    else:
        if flag:
            new=str1+"er"
            print(new)
else:
    print(str1)