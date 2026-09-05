class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res, visit = set(), set()
        #make prefix tree of words
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        #dfs to check all surrounding letters and check if that prefix in the trie
        def dfs(i, j, node, word):
            if ( i< 0 or j<0 or 
                i ==len(board) or j ==len(board[0]) or
                (i, j) in visit or 
                board[i][j] not in node.children):
                return
            visit.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.isWord:
                res.add(word)
            dfs(i-1,j,node, word)
            dfs(i+1,j,node, word)
            dfs(i,j-1,node, word)
            dfs(i,j+1,node, word)
            visit.remove((i,j))
        #go through each cell and dfs
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root, "")

        return list(res)
        