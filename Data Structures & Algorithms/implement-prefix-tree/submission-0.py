class PrefixTree:

    def __init__(self, end=False):
        self.children = {}
        self.end = end
        

    def insert(self, word: str) -> None:
       
        if word == "":
            self.end=True
            return
        if word[:1] in self.children:
            self.children[word[:1]].insert(word[1:])
        else:
            self.children[word[:1]] = PrefixTree()
            self.children[word[:1]].insert(word[1:])
        

    def search(self, word: str) -> bool:
        for c in word:
            if c not in self.children:
                return False
            else:
                self = self.children[c]
        return self.end

    def startsWith(self, prefix: str) -> bool:
        for c in prefix:
            if c not in self.children:
                return False
            else:
                self = self.children[c]
        return True
        