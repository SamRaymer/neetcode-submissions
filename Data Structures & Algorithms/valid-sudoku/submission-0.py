class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        fullSet = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        boardColumns: List[List[str]] = [[] for _ in range(9)]
        subBoards: List[List[List[str]]] = [[[], [], []] for _ in range(3)]
        for i in range(len(board)):
            row = board[i]
            seenInRow = set()
            subBoardYIndex = i // 3
            for j in range(9):
                cur = row[j]
                if cur != "." and cur in seenInRow:
                    return False
                seenInRow.add(cur)
                subBoardXIndex = j // 3
                boardColumns[j].append(cur)
                subBoards[subBoardYIndex][subBoardXIndex].append(cur)
        for col in boardColumns:
            seenInCol = set()
            for i in range(len(col)):
                cur = col[i]
                if cur != "." and cur in seenInCol:
                    return False
                seenInCol.add(cur)
        for boardCol in subBoards:
            for subBoard in boardCol:
                seenInSubBoard = set()
                for i in range(len(subBoard)):
                    cur = subBoard[i]
                    if cur != "." and cur in seenInSubBoard:
                        return False
                    seenInSubBoard.add(cur)

        return True