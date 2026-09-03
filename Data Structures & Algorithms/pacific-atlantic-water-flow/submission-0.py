class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac=set()
        atl=set()
        ret=[]
        def dfs(i,j, seen, prev):
            if i<0 or i>len(heights)-1:
                return
            if j<0 or j>len(heights[0])-1:
                return
            if heights[i][j] < prev:
                return
            if (i,j) in seen:
                return
            seen.add((i,j))
            
            dfs(i-1,j, seen, heights[i][j])
            dfs(i+1,j, seen, heights[i][j])
            dfs(i,j+1, seen, heights[i][j])
            dfs(i,j-1, seen, heights[i][j])

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if(i == 0 or j == 0):     
                    dfs(i,j,pac,0)
                if(i == len(heights)-1 or j == len(heights[0])-1):     
                    dfs(i,j,atl,0)
        for cell in pac & atl:
            ret.append(cell)
        return ret
        