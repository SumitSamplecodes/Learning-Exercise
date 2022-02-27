chessboard = [[0,1,0],[1,0,0],[0,0,0]]


def rooks_are_safe(chessboard):
    n = len(chessboard)
    # check rooks on the same rows if yes return false
    for row_i in range(n):
        row_count = 0
        for col_i in range(n):
            row_count += chessboard[row_i][col_i]
        if row_count > 1:
            return False
    # Check rooks on the same column if yes return false
    for col_i in range(n):
        col_count = 0
        for row_i in range(n):
            col_count += chessboard[row_i][col_i]
        if col_count > 1:
            return False
    return True
