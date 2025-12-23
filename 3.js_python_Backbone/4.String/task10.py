str1=input("Enter a string: ").split(",")
new=''
if len(str1[0])>len(str1[1]):
    for i in range(len(str1[0])):
        if i<=len(str1[1])-1:
            new+=str1[0][i]+str1[1][i]
        else:
            new+=str1[0][i]
else:
    for i in range(len(str1[1])):
        if i<=len(str1[0])-1:
            new+=str1[0][i]+str1[1][i]
        else:
            new+=str1[1][i]
print(new)