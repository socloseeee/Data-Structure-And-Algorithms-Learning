sequence = [5, 1, 3, 2, 4, 6, 1, 7, 3, 2, 8]
m = 3
result = []
for i in range(len(sequence) - m + 1):
    result.append(min(sequence[i: i + m]))
print(result)