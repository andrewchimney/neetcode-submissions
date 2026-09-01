class WordDictionary:

    def __init__(self, end=False):
        self.end = end
        self.children = {}
        
    def addWord(self, word: str) -> None:
        if word =="":
            self.end=True
            return
        if word[0] in self.children:
            self.children[word[0]].addWord(word[1:])
        else:
            self.children[word[0]] = WordDictionary()
            self.children[word[0]].addWord(word[1:])
        

    def search(self, word: str) -> bool:
        if(word==""):
            return self.end
        if word[0] == ".":
            found = False
            for c in self.children:
                found = found or self.children[c].search(word[1:])
            return found

        elif word[0] in self.children:
            return self.children[word[0]].search(word[1:])
       
        return False