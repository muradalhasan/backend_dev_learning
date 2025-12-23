str1=input("Enter a string: ")
new=''
for i in range(len(str1)):
    if i==0:
        new+=str1[i]
    else:
        if str1[i-1]!=str1[i]:
            new+=str1[i]
print(new) 