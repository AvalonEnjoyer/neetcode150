# Empty file to test and delete items over time
from typing import List
def isValidSudoku(board: List[List[str]]) -> bool:
    unique_elements_rows = {}
    unique_elements_cols = {}
    unique_elements_boxes = {}
    for i, row in enumerate(board):
        unique_elements_rows.setdefault(i, [])
        for j in range(len(row)):
            unique_elements_cols.setdefault(j, [])
            if row[j] != ".":
                if row[j] not in unique_elements_rows[i]:
                    unique_elements_rows[i].append(row[j])
                else:
                    return False
                if row[j] not in unique_elements_cols[j]:
                    unique_elements_cols[j].append(row[j])
                else:
                    return False
            if i % 3 == 0:
                row_values = unique_elements_rows[]

    return unique_elements_rows, unique_elements_cols

board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

# board =[["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
