class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        recStack = set()

        graph = {}
        graph = {i: [] for i in range(numCourses)}
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        def dfs(node):
            visited.add(node)
            recStack.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in recStack:
                    return True
            recStack.remove(node)
            return False

        for node in graph:
            if (dfs(node)):
                return False
        
        return True