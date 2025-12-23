exam_marks = {
    'Cierra Vega': 175,
    'Alden Cantrell': 200,
    'Kierra Gentry': 165,
    'Pierre Cox': 190
}

# Take user input
limit = int(input())

# Create new dictionary
result = {}

for key in exam_marks:
    if exam_marks[key] >= limit:
        result[key] = exam_marks[key]

print(result)
