#counts the words contained in a string that it is passed split on all whitespace characters
def wordCount(wordsToCount):
    
    splitBook = wordsToCount.split()
    print(len(splitBook))
    return len(splitBook)
    
def characterCount(charactersToCount):
    charDictionary = {}
    lowerCaseBook = charactersToCount.lower()
    
    tempCount = 0
    
    for charsa in lowerCaseBook:
        #buildKey = charsa + ":"
        
        if charsa in charDictionary:
            
            #Debugging Statements
            ##print("already exists: " + str(tempCount))
            ##tempCount += 1
            continue
        else:
            charDictionary.update({charsa: lowerCaseBook.count(charsa)})
            
            #Debugging Statements
            ##print("added a new value: " + str(tempCount))
            ##tempCount += 1
            
    return charDictionary
        
        
    
    
    
    
    #print(charDictionary)
    
    
    
    