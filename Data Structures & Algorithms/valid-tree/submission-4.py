class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = {}
       
        graph = {i: [] for i in range(n)}
        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        


        def dfs(node, visited, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    if neighbor not in visited:
                            if not dfs(neighbor, visited, node):
                                return False
                    else:
                        return False

            return True

        if not dfs(0, visited, -1):
            return False
        return len(visited) == n