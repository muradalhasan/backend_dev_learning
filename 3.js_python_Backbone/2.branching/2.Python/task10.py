hour=int(input("Enter total working hour: "))

if hour<0 or hour >168:
    print("Invalid working hour")
else:
    if hour<=40:
        print(f"{hour*200}")
    else:
        print(f"{(8000+((hour-4020)*300))}")