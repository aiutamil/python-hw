sequence = [5, 7, 2, 11, 22, 6, 33, 0]

sum, a = 0, 0
while sequence[a] != 0:
    sum += sequence[a]
    a += 1
print('Sum of numbers:', sum)
print('Number of elemets:', a + 1)
