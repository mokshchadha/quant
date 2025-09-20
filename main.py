from typing import List, Dict, Optional, Union, Tuple, Any

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check3x3Board(board) and self.checkRows(board) and self.checkColumns(board)
    
    def check3x3Board(self, board: List[List[str]]) -> bool:
        return False
    
    def checkRows(self, board:List[List[str]]) -> bool:
        return False

    def checkColumns(self, board:List[List[str]]) -> bool:
        return False

    def getIndices(self, index:int) -> List[int]:
        return False
        

def main():
    sol = Solution()
    board = [["1","2",".",".","3",".",".",".","."],
             ["4",".",".","5",".",".",".",".","."],
             [".","9","1",".",".",".",".",".","3"],
             ["5",".",".",".","6",".",".",".","4"],
             [".",".",".","8",".","3",".",".","5"],
             ["7",".",".",".","2",".",".",".","6"],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".","4","1","9",".",".","8"],
             [".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board))
 

if __name__ == "__main__":
    main()
