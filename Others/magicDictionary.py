class MagicDictionary:
    # word = hello dict = { "hullo": 0, "hey": 1 }
    dict = None

    def __init__(self):
        self.dict = {}

    def buildDict(self, dictionary: List[str]) -> None:
        index = 0
        for string in dictionary:
            self.dict[string] = index
            index += 1

    def search(self, searchWord: str) -> bool:
        # iterate through word and check every possible letter in placeholder
        for index, char in enumerate(searchWord): # h in hello
            for i in range(26): # 0
                newChar = i + ord('a') # char = a
                newChar = chr(newChar)
                newWord = ""
                if newChar == char:
                    continue;
                if index == 0:
                    newWord = newChar + searchWord[index + 1:] 
                elif index == len(searchWord) - 1:
                    newWord = searchWord[:-1] + newChar 
                else:
                    newWord = searchWord[:index] + newChar + searchWord[index + 1:] 
                if newWord in self.dict:
                    return True
        return False
                


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)