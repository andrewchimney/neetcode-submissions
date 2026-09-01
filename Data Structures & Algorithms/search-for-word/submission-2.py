class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkCell(board, word, row, col, seen):
            if(word == ""):
                return True
            if(row <0 or col <0 or row>=len(board) or col>=len(board[0]) or (row, col) in seen):
                return False
            if board[row][col]==word[:1]:
                seen.add((row,col))
                found = (

                    checkCell(board, word[1:], row+1, col, seen) or
                    checkCell(board, word[1:], row-1, col, seen) or
                    checkCell(board, word[1:], row, col+1, seen) or
                    checkCell(board, word[1:], row, col-1, seen) 
                )
                seen.remove((row,col))
                return found
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                seen = set()
                if checkCell(board, word, i, j, seen):
                    return True
                    
        return False