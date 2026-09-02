class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        seen = set()
        def dfs(seen, row, col):
            if (row, col) in seen:
                return
            if row <0 or row >=len(grid):
                return
            if col < 0 or col >=len(grid[0]):
                return
            if grid[row][col]=="0":
                return
            seen.add((row,col))
            dfs(seen, row-1, col)
            dfs(seen, row+1, col)
            dfs(seen, row, col-1)
            dfs(seen, row, col+1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col])=="1" and (row, col) not in seen:
                    # seen.add((row, col))
                    count+=1
                    dfs(seen, row, col)
        return count