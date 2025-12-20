inp=int(input("Enter all seconds: "))

rem=inp%3600

print(f" Hours: {inp//3600} Minutes: {rem//60} Seconds: {rem%60}")