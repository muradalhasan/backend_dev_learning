dist=(int(input()))/1000
time=(int(input()))/3600

velocity=dist/time

if velocity<60:
    print("Too slow. Needs more changes.")
elif velocity>=60 and velocity<=90:
    print("Velocity is okay. The car is ready!")
elif velocity >=90:
    print("Too fast. Only a few changes should suffice")