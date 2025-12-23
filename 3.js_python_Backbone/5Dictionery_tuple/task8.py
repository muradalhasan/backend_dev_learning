# Take dictionary input as string
s = input()

data = {}
items = s.split(",")

# Create dictionary
for item in items:
    key_value = item.strip().split(":")
    key = key_value[0].strip()
    value = int(key_value[1].strip())
    data[key] = value

# Calculate sum and count without using sum() or len()
total = 0
count = 0

for value in data.values():
    total += value
    count += 1

average = total // count

print("Average is", average, ".")
