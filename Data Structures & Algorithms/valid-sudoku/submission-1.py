def sqno(x, y):
    return int(x/3) + 3*int(y/3)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0]*9]*9
        cols = [[0]*9]*9
        sqs = [[0]*9]*9
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    # rows
                    if rows[i][int(val)] == 1:
                        return False
                    else: rows[i][int(val)] = 1

                    # cols
                    if cols[j][int(val)] == 1:
                        return False
                    else: cols[j][int(val)] = 1

                    #squares
                    if sqs[sqno(i, j)][int(val)] == 1:
                        return False
                    else: sqs[sqno(i,j)][int(val)] = 1
        return True