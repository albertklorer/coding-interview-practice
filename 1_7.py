import numpy as np

# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 

def rotate(matrix):
    temp = [[0 for col in range(len(matrix))] for row in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp[j][len(matrix) - i - 1] = matrix[i][j]

    return temp

assert rotate([['*', '-'], ['-', '*']]) == [['-', '*'], ['*', '-']]