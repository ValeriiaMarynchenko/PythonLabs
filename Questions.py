from typing import Tuple, List, Any

n = 8
m = 8
tura = "I"
mat = [[]]
for i in range(n - 1):
    for j in range(m - 1):
        if i == 0:
            if j == 0:
                mat[i][j] = tura
            elif j == 7:
                mat[i][j] = tura
            else:
                mat[i][j] = "_"
        elif i == 7:
            if j == 0:
                mat[i][j] = tura
            elif j == 7:
                mat[i][j] = tura
            else:
                mat[i][j] = "_"
        else:
            mat[i][j] = "_"
for row in mat:
    print(' '.join([str(elem) for elem in row]))