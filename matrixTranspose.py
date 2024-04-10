import numpy as np

matrix = np.random.randint(0, 3, size = (5, 5))

print("\nMatrix: ")
for row in matrix:
    print(row)

transpose = np.transpose(matrix)
print("\nTranspose: ")
for row in transpose:
    print(row)