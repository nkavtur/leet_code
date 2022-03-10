def rotate(matrix):
    n = len(matrix)
    layers_num = n // 2

    for i in range(0, layers_num):
        for j in range(0 + i, n - i - 1):
            left = matrix[n - 1 - j][i]
            top = matrix[i][j]
            right = matrix[j][n - 1 - i]
            bottom = matrix[n - 1 - i][n - 1 - j]

            matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j] = bottom, left, top, right

    return matrix


print(rotate([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))
