# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 

def change(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                for j in range(len(matrix)):
                    matrix[i][j] = 0
                break

    return matrix

assert change([[1, 0], [1, 1]]) == change([[0, 0], [1, 1]])