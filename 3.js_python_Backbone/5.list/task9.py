# Take input as a string
s = input()

numbers = []
num = ""

# Manually parse the string (without split)
for ch in s:
    if ch != " ":
        num += ch
    else:
        numbers.append(int(num))
        num = ""

# Add the last number
if num:
    numbers.append(int(num))

print("Original list:", numbers)

# Remove even numbers
modified_list = []
for n in numbers:
    if n % 2 != 0:
        modified_list.append(n)

print("Modified list:", modified_list)
