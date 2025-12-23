# Given dictionary (you can change this to test other cases)
books = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure': 14}

# Initialize variables
highest_key = None
highest_value = None

# Find the largest value manually
for key in books:
    if highest_value is None or books[key] > highest_value:
        highest_value = books[key]
        highest_key = key

# Print result
print(f"The highest selling book genre is '{highest_key}' and the number of books sold are {highest_value}.")
