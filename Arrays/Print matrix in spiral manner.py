def printSpiral(matrix):
    if not matrix:
        return
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Left → Right
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1

        # Top → Bottom
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        # Right → Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        # Bottom → Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1


# ------------ INPUT SECTION ------------

n, m = map(int, input("Enter rows and columns: ").split())

matrix = []
print("Enter matrix values:")

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# ------------ OUTPUT ------------

print("Spiral order:")
printSpiral(matrix)
