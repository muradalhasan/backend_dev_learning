hour=int(input("ENter hours: "))

if hour>23 or hour <0:
    print("Wrong TIme")
else:
    if hour>=4 and hour<=5:
        print("Breakfast")
    elif hour>=12 and hour<=13:
        print("Lunch")
    elif hour>=16 and hour<=17:
        print("Snacks")
    elif hour>=19 and hour<=20:
        print("Dinner")
    else:
        print("Patient is a virtue")