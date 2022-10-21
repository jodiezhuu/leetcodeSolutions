def longestWord(words) -> str:
    # store words in dictionary 
    hashWords = {}
    index = 0 
    for word in words:# O(n)
        hashWords[word] = index
        index += 1
    currLongestString = ""
    # iterate through each word in words and string splice to check if each possible prefix is in the dictionary
    for word in words:
        prefixExists = True
        for i in range(len(word) - 1):
            s = word[0:i + 1]
            if s not in hashWords:
                prefixExists = False
        if prefixExists:
            if len(word) > len(currLongestString):
                currLongestString = word
            elif len(word) == len(currLongestString) and word < currLongestString:
                currLongestString = word
    return currLongestString

words = ["a","banana","app","appl","ap","apply","apple"]  
words2 = ["a", "a", "a"]    
assert longestWord(words) == "apple"
assert len(longestWord(words2)) == len("a")