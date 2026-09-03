class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()

        graph = {i: [] for i in range(n)}

        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
     
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
      
            # for neighbor in graph[node]:
            #     if neighbor in visited:
                   
            #         break
          
            for neighbor in graph[node]:
                dfs(neighbor)


        for node in range(n):
            if node not in visited:
                count+=1
            dfs(node)
        return count


