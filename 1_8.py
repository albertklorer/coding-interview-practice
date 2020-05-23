# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0. 

def change(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                for j in range(len(matrix)):
                    matrix[i][j] = 0
                break

    return matrix

assert change([[1, 0], [1, 1]]) == change([[0, 0], [1, 1]])