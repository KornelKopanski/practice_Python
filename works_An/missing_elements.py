

collection10_20 = [12,14,13,17,19,18]

missing_elements = []

element = 10

while element != 21:
    if element not in collection10_20:
        missing_elements.append(element)

    element += 1

print(missing_elements)