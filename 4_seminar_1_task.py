* Напишите функцию для транспонирования матрицы


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12,],
          [13, 14, 15, 16]]
new_matrix = []
          
def transposition(matrix):
    new_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return(new_matrix)
    
new_matrix = transposition(matrix)
for i in new_matrix:
    print(*i)