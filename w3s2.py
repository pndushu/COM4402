"""
rows = 5

for i in range(1, rows + 1):
    print('*' * i)
    """
#practice 2
"""
rows = 5

for i in range(1, rows + 1):
    print(str(i) * i)
    """
"""
#practice 3
rows = 4
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end="")
        num += 1
    print()
"""
#practice 4
""""
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:3}", end=" ")
    print()
    """
#practice 5
    """
for row in range(3):
    for col in range(4):
        print(f"({row},{col})", end=" ")
    print()
"""
"""
size = 5

for row in range(size):
    if row == 0 or row == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")


#practice7
rows = 4

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
"""
#practice8
"""
for i in range(1, 6):
    for n in range(2, 5):
        result = n * i
        print(f"{n} x {i} = {result:2}", end=" ")
    print()
    """
#practice 9
"""
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()
    """
#practice 10
"""
rows = 5
triangle = []

for i in range(rows):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for row in triangle:
    print(*row)
    """




















