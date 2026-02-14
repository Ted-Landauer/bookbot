#counts the words contained in a string that it is passed split on all whitespace characters
def wordCount(wordsToCount):
    
    splitBook = wordsToCount.split()
    #print(len(splitBook))
    return len(splitBook)
    
#count the number of times characters repeat
def characterCount(charactersToCount):
    charDictionary = {}
    lowerCaseBook = charactersToCount.lower()
    
    tempCount = 0
    
    for charsa in lowerCaseBook:
        
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
    
    
#sort the character repitition count
def sortedDictionary(dictToSort):
    
    filtered_dict = []
    
    for char, count in dictToSort.items():
        if char.isalpha():
            filtered_dict.append((char, count))
    
    sorted_dict = dict(sorted(filtered_dict, key=dictSortHelper, reverse=True))
    
    return sorted_dict
        

#sorting helper function 
def dictSortHelper(items):
    
    return items[1]
    
    
    
    
    
    