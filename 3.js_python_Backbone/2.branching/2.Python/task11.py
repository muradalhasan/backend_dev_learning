inpS=int(input())

if inpS>=100:
    l=(12000)/(4+((inpS**2)/14900))
    print(l)
else:
    l=3000-(125*(inpS**2))
    print(l)