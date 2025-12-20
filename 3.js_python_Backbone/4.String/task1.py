str1=input("Enter a string: ")

new=''
for i in range(len(str1)-1,-1,-1):
    new+=str1[i]
print(new)