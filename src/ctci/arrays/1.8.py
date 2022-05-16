def zero_row(matrix, row_index):
    matrix[row_index] = [0] * len(matrix[0])


def zero_column(matrix, column_index):
    for i in range(0, len(matrix)):
        matrix[i][column_index] = 0


def zero_matrix(matrix):
    n, m = len(matrix), len(matrix[0])

    storage_row_index = None
    for i in range(0, n):
        if all(matrix[i]):
            storage_row_index = i
            break

    # all rows contain 0 - zero matrix
    if not storage_row_index:
        for i in range(0, n):
            zero_row(matrix, i)
        return matrix

    # rows handling
    for i in range(0, n):
        if i == storage_row_index:
            continue

        is_zero_row = not all(matrix[i])
        if is_zero_row:
            for j in range(0, m):
                if matrix[i][j] == 0:
                    matrix[storage_row_index][j] = 0
            zero_row(matrix, i)

    # cols handling:
    for col_index, value in enumerate(matrix[storage_row_index]):
        if value == 0:
            zero_column(matrix, col_index)

    return matrix


print(zero_matrix([
    [1, 2, 3, 4, 0],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 0, 18, 19, 20],
    [21, 22, 23, 24, 25],
]))
