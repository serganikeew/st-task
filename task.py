mass1 = [1, 2, 3, 4, 5, 6]
mass2 = [10, 9, 8, 7, 6, 5]
intersection = []

for i in mass1:
    if i in mass2:
        intersection.append(i)

print(intersection)
