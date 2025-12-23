lst=[]
while True:
    n=int(input("Enter a number : "))
    if n==0:
        lst.append(n)
        print(f"Numbers in the list: {lst}")
        break
    lst.append(n)
    print(f"Numbers in the list: {lst}")
