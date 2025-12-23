s = input().lower()

freq = {}

for ch in s:
    if ch != " ":
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

print(freq)
