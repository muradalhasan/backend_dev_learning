str1=input("Enter a string: ")
new=''
for i in range(len(str1)):
    if i%2!=0:
        new+=str1[i].upper()
print(new)