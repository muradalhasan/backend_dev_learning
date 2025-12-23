str1=input("Enter a string: ").lower()
new=''
for i in str1:
    if ord(i)==122:
        new+=chr(97)
    else:
        new+=chr(ord(i)+1)
print(new)