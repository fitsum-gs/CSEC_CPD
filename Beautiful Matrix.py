matrix=[list(map(int,input().split())) for i in range(5)]
def min_moves(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==1:
                row,col=i,j
                break
    print(abs(row-2)+abs(col-2))
min_moves(matrix)
